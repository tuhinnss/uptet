import 'dart:math';

import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/attempt.dart';
import '../models/content.dart';
import '../widgets/test_settings_sheet.dart';
import 'quiz_screen.dart';

/// Asks for practice or mock test settings, then starts the paper. The
/// unfinished attempt [replacing] is discarded only once settings are chosen,
/// so dismissing the sheet keeps it.
Future<void> startPaper(BuildContext context, Paper paper, {int? replacing}) async {
  final app = AppScope.read(context);
  final questions = app.content.questionsForPaper(paper.id);
  // Papers without a stated duration get a minute per question.
  final fullMinutes = paper.durationMinutes ?? questions.length;
  final settings = await showTestSettingsSheet(context, fullMinutes: fullMinutes);
  if (settings == null || !context.mounted) return;
  if (replacing != null) await app.progress.discardInProgress(replacing);
  if (!context.mounted) return;
  await startQuiz(
    context,
    kind: AttemptKind.paper,
    paperId: paper.id,
    questions: settings.shuffle ? ([...questions]..shuffle(Random())) : questions,
    marking: settings.markingFor(paper.marking),
    mode: settings.mode,
    timeLimit: settings.timeLimitFor(fullMinutes),
  );
}

/// Creates a new attempt and opens it.
Future<void> startQuiz(
  BuildContext context, {
  required AttemptKind kind,
  String? paperId,
  String? topicId,
  required List<Question> questions,
  required MarkingScheme marking,
  AttemptMode mode = AttemptMode.practice,
  Duration? timeLimit,
}) async {
  final app = AppScope.read(context);
  final s = S.of(context);
  final messenger = ScaffoldMessenger.of(context);
  final int attemptId;
  try {
    attemptId = await app.progress.startAttempt(
      kind: kind,
      paperId: paperId,
      topicId: topicId,
      questions: questions,
      marking: marking,
      contentVersion: app.content.contentVersion,
      mode: mode,
      timeLimit: timeLimit,
    );
  } catch (e) {
    debugPrint('Could not start attempt: $e');
    messenger.showSnackBar(SnackBar(content: Text(s.couldNotStart)));
    return;
  }
  app.progressChanged();
  if (context.mounted) await QuizScreen.open(context, attemptId);
}

/// Topic practice: offers to resume an unfinished attempt before starting anew.
Future<void> startOrResumeTopic(BuildContext context, Topic topic) async {
  final app = AppScope.read(context);
  final s = S.of(context);
  final unfinished = await app.progress.inProgressFor(topicId: topic.id);
  if (!context.mounted) return;
  if (unfinished != null) {
    final choice = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(s.unfinishedPractice),
        content: Text(s.stoppedAt(unfinished.currentIndex + 1, unfinished.totalQuestions)),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context, false), child: Text(s.startAgain)),
          FilledButton(onPressed: () => Navigator.pop(context, true), child: Text(s.resume)),
        ],
      ),
    );
    if (choice == null || !context.mounted) return;
    if (choice) {
      await QuizScreen.open(context, unfinished.id);
      return;
    }
    await app.progress.discardInProgress(unfinished.id);
    if (!context.mounted) return;
  }
  await startQuiz(
    context,
    kind: AttemptKind.topic,
    topicId: topic.id,
    questions: app.content.questionsForTopic(topic.id),
    marking: MarkingScheme.oneMarkNoNegative,
  );
}
