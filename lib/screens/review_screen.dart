import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/revision.dart';
import '../repositories/progress_repository.dart';
import '../services/revision_scheduler.dart';
import '../widgets/common.dart';
import '../widgets/feedback.dart';
import '../widgets/question_view.dart';

/// Works through the questions due for revision, one at a time. Each answer
/// is saved as soon as it is checked, so stopping halfway loses nothing.
class ReviewScreen extends StatefulWidget {
  const ReviewScreen({super.key});

  static Future<void> open(BuildContext context) =>
      Navigator.of(context, rootNavigator: true).push(
        MaterialPageRoute<void>(builder: (_) => const ReviewScreen()),
      );

  @override
  State<ReviewScreen> createState() => _ReviewScreenState();
}

class _ReviewScreenState extends State<ReviewScreen> {
  List<RevisionItem>? _items;
  bool _started = false;
  bool _failed = false;
  int _index = 0;
  String? _selected;
  ReviewOutcome? _outcome;
  int _correct = 0;
  bool _saving = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (!_started) {
      _started = true;
      _load();
    }
  }

  Future<void> _load() async {
    final app = AppScope.read(context);
    try {
      final due = await app.progress.dueRevisionItems();
      if (mounted) {
        setState(() => _items = [for (final item in due) if (app.content.question(item.questionId) != null) item]);
      }
    } catch (e) {
      debugPrint('Could not load revision: $e');
      if (mounted) setState(() => _failed = true);
    }
  }

  Future<void> _check() async {
    final app = AppScope.read(context);
    final selected = _selected;
    if (selected == null) return;
    setState(() => _saving = true);
    try {
      final outcome = await app.progress.recordReview(_items![_index].id, selected, app.content);
      if (!mounted) return;
      setState(() {
        _outcome = outcome;
        if (outcome.isCorrect) _correct++;
      });
      app.progressChanged();
    } catch (e) {
      debugPrint('Could not save review: $e');
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(S.of(context).reviewSaveFailed)));
      }
    } finally {
      if (mounted) setState(() => _saving = false);
    }
  }

  void _next() => setState(() {
        _index++;
        _selected = null;
        _outcome = null;
      });

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final items = _items;

    Widget body;
    Widget? bottom;
    if (_failed) {
      body = LoadError(onRetry: () {
        setState(() => _failed = false);
        _load();
      });
    } else if (items == null) {
      body = const Center(child: CircularProgressIndicator());
    } else if (items.isEmpty) {
      body = EmptyState(icon: Icons.check_circle_outline, title: s.nothingDue);
    } else if (_index >= items.length) {
      body = EmptyState(
        icon: Icons.emoji_events_outlined,
        title: s.reviewSummary(_correct, items.length),
        action: FilledButton(onPressed: () => Navigator.of(context).pop(), child: Text(s.finish)),
      );
    } else {
      final item = items[_index];
      final question = app.content.question(item.questionId)!;
      final outcome = _outcome;
      body = SingleChildScrollView(
        key: ValueKey(item.id),
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            QuestionView(
              question: question,
              heading:
                  '${s.questionXofY(_index + 1, items.length)} · ${s.reviewStep(item.state.stage, app.progress.scheduler.reviewsToMaster)}',
              selectedOptionId: _selected,
              onSelect: outcome == null && !_saving ? (id) => setState(() => _selected = id) : null,
              correctOptionId: outcome == null ? null : question.correctOptionId,
              showExplanation: outcome != null,
            ),
            if (outcome != null) ...[
              const SizedBox(height: 12),
              _Feedback(outcome: outcome),
              ReportQuestionButton(questionId: question.id),
            ],
          ],
        ),
      );
      final isLast = _index == items.length - 1;
      bottom = SafeArea(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(16, 8, 16, 12),
          child: FilledButton(
            style: FilledButton.styleFrom(minimumSize: const Size.fromHeight(48)),
            onPressed: outcome != null
                ? _next
                : (_selected == null || _saving)
                    ? null
                    : _check,
            child: Text(outcome == null ? s.checkAnswer : (isLast ? s.finish : s.next)),
          ),
        ),
      );
    }

    return Scaffold(
      appBar: AppBar(title: Text(s.revision)),
      body: body,
      bottomNavigationBar: bottom,
    );
  }
}

class _Feedback extends StatelessWidget {
  const _Feedback({required this.outcome});

  final ReviewOutcome outcome;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final theme = Theme.of(context);
    final color = outcome.isCorrect ? FeedbackColors.correct(context) : FeedbackColors.wrong(context);
    final next = outcome.state.status == RevisionStatus.mastered
        ? s.masteredFeedback
        : s.seeAgainIn(calendarDaysBetween(DateTime.now(), outcome.state.nextReviewAt));
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        border: Border.all(color: color, width: 2),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(outcome.isCorrect ? Icons.check_circle : Icons.cancel, color: color),
          const SizedBox(width: 10),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(outcome.isCorrect ? s.rightFeedback : s.wrongFeedback,
                    style: theme.textTheme.titleSmall?.copyWith(color: color)),
                const SizedBox(height: 4),
                Text(next),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
