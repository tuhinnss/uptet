import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/attempt.dart';
import '../models/content.dart';
import '../widgets/common.dart';
import '../widgets/question_view.dart';
import '../widgets/settings_sheet.dart';
import 'result_screen.dart';

/// Answers a paper or topic attempt. Every choice is saved as it is made, so
/// leaving the screen never loses work; only an explicit, confirmed submit
/// ends the attempt.
class QuizScreen extends StatefulWidget {
  const QuizScreen({super.key, required this.attemptId});

  final int attemptId;

  static Future<void> open(BuildContext context, int attemptId) => Navigator.of(context).push(
        MaterialPageRoute<void>(builder: (_) => QuizScreen(attemptId: attemptId)),
      );

  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> {
  Attempt? _attempt;
  List<Question> _questions = const [];
  final Map<String, String?> _selected = {};
  int _index = 0;
  bool _started = false;
  bool _failed = false;
  bool _submitting = false;

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
      final attempt = await app.progress.loadAttempt(widget.attemptId);
      if (attempt == null) throw StateError('Attempt ${widget.attemptId} not found');
      if (!mounted) return;
      if (attempt.isSubmitted) {
        ResultScreen.replace(context, attempt.id);
        return;
      }
      final questions = [
        for (final id in attempt.questionIds)
          app.content.question(id) ?? (throw StateError('Question $id is not installed')),
      ];
      if (questions.isEmpty) throw StateError('Attempt ${attempt.id} has no questions');
      setState(() {
        _attempt = attempt;
        _questions = questions;
        _selected.addAll({for (final a in attempt.answers.values) a.questionId: a.selectedOptionId});
        _index = attempt.currentIndex.clamp(0, questions.length - 1);
      });
    } catch (e) {
      debugPrint('Could not open attempt: $e');
      if (mounted) setState(() => _failed = true);
    }
  }

  int get _answeredCount => _selected.values.where((v) => v != null).length;

  Future<void> _select(String optionId) async {
    final app = AppScope.read(context);
    final questionId = _questions[_index].id;
    final previous = _selected[questionId];
    setState(() => _selected[questionId] = optionId);
    try {
      await app.progress.saveAnswer(widget.attemptId, questionId, optionId);
    } catch (e) {
      debugPrint('Could not save answer: $e');
      if (!mounted) return;
      if (_selected[questionId] == optionId) setState(() => _selected[questionId] = previous);
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(S.of(context).answerSaveFailed)));
    }
  }

  void _goTo(int index) {
    setState(() => _index = index);
    _saveIndex(index);
  }

  Future<void> _saveIndex(int index) async {
    try {
      await AppScope.read(context).progress.saveCurrentIndex(widget.attemptId, index);
    } catch (e) {
      // Only the resume position is lost; answers are saved separately.
      debugPrint('Could not save position: $e');
    }
  }

  Future<void> _confirmLeave() async {
    final s = S.of(context);
    final app = AppScope.read(context);
    final leave = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(s.leaveTitle),
        content: Text(s.leaveBody),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context, true), child: Text(s.leave)),
          FilledButton(onPressed: () => Navigator.pop(context, false), child: Text(s.stay)),
        ],
      ),
    );
    if (leave != true || !mounted) return;
    app.progressChanged();
    Navigator.of(context).pop();
  }

  Future<void> _confirmSubmit() async {
    final s = S.of(context);
    final app = AppScope.read(context);
    final answered = _answeredCount;
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(s.submitTitle),
        content: Text(s.submitBody(answered, _questions.length - answered)),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context, false), child: Text(s.cancel)),
          FilledButton(onPressed: () => Navigator.pop(context, true), child: Text(s.submit)),
        ],
      ),
    );
    if (confirmed != true || !mounted) return;

    setState(() => _submitting = true);
    try {
      await app.progress.submitAttempt(widget.attemptId, app.content);
    } catch (e) {
      debugPrint('Could not submit attempt: $e');
      if (!mounted) return;
      setState(() => _submitting = false);
      await showDialog<void>(
        context: context,
        builder: (context) => AlertDialog(
          content: Text(s.submitFailed),
          actions: [FilledButton(onPressed: () => Navigator.pop(context), child: Text(s.ok))],
        ),
      );
      return;
    }
    app.progressChanged();
    if (mounted) ResultScreen.replace(context, widget.attemptId, justSubmitted: true);
  }

  void _showQuestionGrid() {
    final s = S.of(context);
    showModalBottomSheet<void>(
      context: context,
      showDragHandle: true,
      isScrollControlled: true,
      builder: (sheetContext) {
        final theme = Theme.of(sheetContext);
        final scheme = theme.colorScheme;
        return SafeArea(
          child: Padding(
            padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Text(s.allQuestions, style: theme.textTheme.titleMedium),
                const SizedBox(height: 4),
                Text('${s.answered}: $_answeredCount / ${_questions.length}', style: theme.textTheme.bodyMedium),
                const SizedBox(height: 12),
                Flexible(
                  child: SingleChildScrollView(
                    child: Wrap(
                      spacing: 8,
                      runSpacing: 8,
                      children: [
                        for (var i = 0; i < _questions.length; i++)
                          _GridCell(
                            number: i + 1,
                            answered: _selected[_questions[i].id] != null,
                            current: i == _index,
                            scheme: scheme,
                            onTap: () {
                              Navigator.pop(sheetContext);
                              _goTo(i);
                            },
                          ),
                      ],
                    ),
                  ),
                ),
                const SizedBox(height: 16),
                FilledButton.icon(
                  onPressed: () {
                    Navigator.pop(sheetContext);
                    _confirmSubmit();
                  },
                  icon: const Icon(Icons.check),
                  label: Text(s.submitTest),
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final attempt = _attempt;
    if (_failed) {
      return Scaffold(appBar: AppBar(), body: EmptyState(icon: Icons.error_outline, title: s.testUnavailable));
    }
    if (attempt == null) {
      return Scaffold(appBar: AppBar(), body: const Center(child: CircularProgressIndicator()));
    }

    final question = _questions[_index];
    final isLast = _index == _questions.length - 1;
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, _) {
        if (!didPop) _confirmLeave();
      },
      child: Scaffold(
        appBar: AppBar(
          title: Text(attemptTitle(context, attempt), maxLines: 1, overflow: TextOverflow.ellipsis),
          actions: [
            const LanguageButton(),
            IconButton(tooltip: s.allQuestions, icon: const Icon(Icons.grid_view), onPressed: _showQuestionGrid),
          ],
          bottom: PreferredSize(
            preferredSize: const Size.fromHeight(4),
            child: LinearProgressIndicator(value: _answeredCount / _questions.length),
          ),
        ),
        body: SingleChildScrollView(
          key: ValueKey(question.id),
          padding: const EdgeInsets.all(16),
          child: QuestionView(
            question: question,
            heading: s.questionXofY(_index + 1, _questions.length),
            selectedOptionId: _selected[question.id],
            onSelect: _submitting ? null : _select,
          ),
        ),
        bottomNavigationBar: SafeArea(
          child: Padding(
            padding: const EdgeInsets.fromLTRB(16, 8, 16, 12),
            child: Row(
              children: [
                Expanded(
                  child: OutlinedButton.icon(
                    style: OutlinedButton.styleFrom(minimumSize: const Size.fromHeight(48)),
                    onPressed: _index == 0 ? null : () => _goTo(_index - 1),
                    icon: const Icon(Icons.chevron_left),
                    label: Text(s.previous),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: isLast
                      ? FilledButton.icon(
                          style: FilledButton.styleFrom(minimumSize: const Size.fromHeight(48)),
                          onPressed: _submitting ? null : _confirmSubmit,
                          icon: const Icon(Icons.check),
                          label: Text(s.submit),
                        )
                      : FilledButton.icon(
                          style: FilledButton.styleFrom(minimumSize: const Size.fromHeight(48)),
                          onPressed: () => _goTo(_index + 1),
                          icon: const Icon(Icons.chevron_right),
                          label: Text(s.next),
                        ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _GridCell extends StatelessWidget {
  const _GridCell({
    required this.number,
    required this.answered,
    required this.current,
    required this.scheme,
    required this.onTap,
  });

  final int number;
  final bool answered;
  final bool current;
  final ColorScheme scheme;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    return Material(
      color: answered ? scheme.primary : Colors.transparent,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(10),
        side: BorderSide(color: current ? scheme.tertiary : scheme.outline, width: current ? 3 : 1),
      ),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(10),
        child: SizedBox(
          width: 48,
          height: 48,
          child: Center(
            child: Text(
              '$number',
              style: TextStyle(
                color: answered ? scheme.onPrimary : scheme.onSurface,
                fontWeight: answered ? FontWeight.bold : FontWeight.normal,
              ),
            ),
          ),
        ),
      ),
    );
  }
}
