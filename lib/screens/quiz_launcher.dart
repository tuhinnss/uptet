import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/attempt.dart';
import '../models/content.dart';
import 'quiz_screen.dart';

/// Creates a new attempt and opens it.
Future<void> startQuiz(
  BuildContext context, {
  required AttemptKind kind,
  String? paperId,
  String? topicId,
  required List<Question> questions,
  required MarkingScheme marking,
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
