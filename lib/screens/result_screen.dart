import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/attempt.dart';
import '../widgets/async_loader.dart';
import '../widgets/common.dart';
import '../widgets/feedback.dart';
import '../widgets/question_view.dart';

enum _Filter { all, incorrect, unanswered }

/// Score, breakdown and answer review of a submitted attempt. Uses the values
/// stored at submission, so reopening an old attempt shows its original result.
class ResultScreen extends StatefulWidget {
  const ResultScreen({super.key, required this.attemptId, this.justSubmitted = false});

  final int attemptId;
  final bool justSubmitted;

  static Future<void> open(BuildContext context, int attemptId) =>
      Navigator.of(context, rootNavigator: true).push(
        MaterialPageRoute<void>(builder: (_) => ResultScreen(attemptId: attemptId)),
      );

  static void replace(BuildContext context, int attemptId, {bool justSubmitted = false}) =>
      Navigator.of(context).pushReplacement(MaterialPageRoute<void>(
        builder: (_) => ResultScreen(attemptId: attemptId, justSubmitted: justSubmitted),
      ));

  @override
  State<ResultScreen> createState() => _ResultScreenState();
}

class _ResultScreenState extends State<ResultScreen> {
  _Filter _filter = _Filter.all;

  bool _matches(AnswerRecord? answer) => switch (_filter) {
        _Filter.all => true,
        _Filter.incorrect => answer != null && answer.isAnswered && answer.isCorrect == false,
        _Filter.unanswered => answer == null || !answer.isAnswered,
      };

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    return Scaffold(
      appBar: AppBar(title: Text(s.result)),
      body: AsyncLoader<Attempt>(
        load: (app) async =>
            await app.progress.loadAttempt(widget.attemptId) ?? (throw StateError('Attempt ${widget.attemptId} not found')),
        builder: (context, attempt) {
          final app = AppScope.of(context);
          if (!attempt.isSubmitted) {
            return EmptyState(icon: Icons.hourglass_empty, title: s.testUnavailable);
          }
          final visible = [
            for (final (i, id) in attempt.questionIds.indexed)
              if (_matches(attempt.answers[id]) && app.content.question(id) != null) (i, id),
          ];
          return ListView.builder(
            padding: const EdgeInsets.all(16),
            itemCount: visible.length + 2,
            itemBuilder: (context, item) {
              if (item == 0) return _Summary(attempt: attempt, justSubmitted: widget.justSubmitted);
              if (item == 1) {
                return Padding(
                  padding: const EdgeInsets.symmetric(vertical: 16),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      SegmentedButton<_Filter>(
                        showSelectedIcon: false,
                        segments: [
                          ButtonSegment(value: _Filter.all, label: Text(s.all)),
                          ButtonSegment(value: _Filter.incorrect, label: Text('${s.incorrect} (${attempt.incorrectCount ?? 0})')),
                          ButtonSegment(value: _Filter.unanswered, label: Text('${s.notAnswered} (${attempt.unansweredCount ?? 0})')),
                        ],
                        selected: {_filter},
                        onSelectionChanged: (selection) => setState(() => _filter = selection.first),
                      ),
                      if (visible.isEmpty)
                        Padding(
                          padding: const EdgeInsets.only(top: 24),
                          child: Text(s.nothingInFilter, textAlign: TextAlign.center),
                        ),
                    ],
                  ),
                );
              }
              final (index, questionId) = visible[item - 2];
              final question = app.content.question(questionId)!;
              final answer = attempt.answers[questionId];
              return Card(
                margin: const EdgeInsets.only(bottom: 12),
                child: Padding(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      QuestionView(
                        question: question,
                        heading: s.questionXofY(index + 1, attempt.totalQuestions),
                        selectedOptionId: answer?.selectedOptionId,
                        correctOptionId: answer?.correctOptionId ?? question.correctOptionId,
                        showExplanation: true,
                      ),
                      ReportQuestionButton(questionId: question.id),
                    ],
                  ),
                ),
              );
            },
          );
        },
      ),
      bottomNavigationBar: SafeArea(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(16, 8, 16, 12),
          child: FilledButton(
            style: FilledButton.styleFrom(minimumSize: const Size.fromHeight(48)),
            onPressed: () => Navigator.of(context).pop(),
            child: Text(s.done),
          ),
        ),
      ),
    );
  }
}

class _Summary extends StatelessWidget {
  const _Summary({required this.attempt, required this.justSubmitted});

  final Attempt attempt;
  final bool justSubmitted;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final theme = Theme.of(context);
    final incorrect = attempt.incorrectCount ?? 0;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Text(attemptTitle(context, attempt), style: theme.textTheme.titleMedium),
        Text(s.submittedOn(formatDateTime(context, attempt.submittedAt!)), style: theme.textTheme.bodySmall),
        if (attempt.mode == AttemptMode.mock) ...[
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: InfoChip(icon: Icons.timer_outlined, label: '${s.modeMock} · ${s.marking(attempt.marking)}'),
          ),
        ],
        const SizedBox(height: 16),
        Text(s.score, style: theme.textTheme.labelLarge),
        Text(attemptScore(attempt), style: theme.textTheme.displaySmall),
        const SizedBox(height: 16),
        StatGrid(tiles: [
          StatTile(label: s.correct, value: '${attempt.correctCount ?? 0}'),
          StatTile(label: s.incorrect, value: '$incorrect'),
          StatTile(label: s.notAnswered, value: '${attempt.unansweredCount ?? 0}'),
          StatTile(label: s.accuracy, value: formatPercent(attempt.accuracyPercent)),
          // Attempts from before the clock was recorded have no time.
          if (attempt.elapsed > Duration.zero)
            StatTile(
              label: s.timeTaken,
              value: attempt.timeLimit == null
                  ? formatClock(attempt.elapsed)
                  : s.ofTimeLimit(formatClock(attempt.elapsed), attempt.timeLimit!.inMinutes),
            ),
        ]),
        if (justSubmitted && incorrect > 0) ...[
          const SizedBox(height: 16),
          NoticeBanner(icon: Icons.replay, text: s.addedToRevision(incorrect)),
        ],
      ],
    );
  }
}
