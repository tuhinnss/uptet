import 'dart:async';

import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/attempt.dart';
import '../models/content.dart';
import '../repositories/progress_repository.dart';
import '../theme.dart';
import '../widgets/brand.dart';
import '../widgets/common.dart';
import '../widgets/question_view.dart';
import '../widgets/settings_sheet.dart';
import 'result_screen.dart';

/// Answers a paper or topic attempt. Every choice is saved as it is made, so
/// leaving the screen never loses work; only an explicit, confirmed submit
/// ends the attempt, or the clock running out in a mock test.
///
/// The clock only runs while this screen is open and the app is in the
/// foreground, so a phone call or leaving the test does not use up time.
class QuizScreen extends StatefulWidget {
  const QuizScreen({super.key, required this.attemptId});

  final int attemptId;

  static Future<void> open(BuildContext context, int attemptId) =>
      Navigator.of(context, rootNavigator: true).push(
        MaterialPageRoute<void>(builder: (_) => QuizScreen(attemptId: attemptId)),
      );

  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> with WidgetsBindingObserver {
  static const _saveClockEvery = Duration(seconds: 15);

  Attempt? _attempt;
  List<Question> _questions = const [];
  final Map<String, String?> _selected = {};
  int _index = 0;
  bool _started = false;
  bool _failed = false;
  bool _submitting = false;
  bool _showExplanation = false;

  // Kept for dispose, when the context can no longer be used.
  ProgressRepository? _progress;
  Duration _elapsedBefore = Duration.zero;
  final Stopwatch _clock = Stopwatch();
  Timer? _ticker;
  Duration _lastSaved = Duration.zero;

  Duration get _elapsed {
    final elapsed = _elapsedBefore + _clock.elapsed;
    final limit = _attempt?.timeLimit;
    return limit != null && elapsed > limit ? limit : elapsed;
  }

  Duration? get _remaining {
    final limit = _attempt?.timeLimit;
    return limit == null ? null : limit - _elapsed;
  }

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    if (!_started) {
      _started = true;
      _progress = AppScope.read(context).progress;
      _load();
    }
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    _pauseClock();
    super.dispose();
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.resumed) {
      _resumeClock();
    } else {
      _pauseClock();
    }
  }

  void _resumeClock() {
    if (_attempt == null || _submitting || _clock.isRunning) return;
    _clock.start();
    _ticker = Timer.periodic(const Duration(seconds: 1), (_) => _tick());
  }

  void _pauseClock() {
    if (!_clock.isRunning) return;
    _clock.stop();
    _ticker?.cancel();
    _ticker = null;
    _saveClock();
  }

  void _tick() {
    if (!mounted) return;
    final remaining = _remaining;
    if (remaining != null && remaining <= Duration.zero) {
      _timeUp();
      return;
    }
    if (_attempt!.isTimed) setState(() {});
    if (_elapsed - _lastSaved >= _saveClockEvery) _saveClock();
  }

  Future<void> _saveClock() async {
    final elapsed = _elapsed;
    _lastSaved = elapsed;
    try {
      await _progress?.saveElapsed(widget.attemptId, elapsed);
    } catch (e) {
      // At most the last few seconds are lost; the clock carries on.
      debugPrint('Could not save time: $e');
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
        _elapsedBefore = _lastSaved = attempt.elapsed;
      });
      // A mock test whose time ran out before it could be submitted is submitted now.
      if (_remaining case final remaining? when remaining <= Duration.zero) {
        _timeUp();
      } else {
        _resumeClock();
      }
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
    setState(() {
      _index = index;
      _showExplanation = false;
    });
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
        content: Text(_attempt!.isTimed ? s.mockLeaveBody : s.leaveBody),
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
    await _submit(app, s);
  }

  /// Ends a mock test when its time runs out. The answers given so far count.
  Future<void> _timeUp() async {
    if (_submitting || !mounted) return;
    final app = AppScope.read(context);
    final s = S.of(context);
    final messenger = ScaffoldMessenger.of(context);
    // Close any open dialog or sheet so the result replaces this screen, not them.
    final route = ModalRoute.of(context);
    Navigator.of(context).popUntil((r) => r == route);
    if (await _submit(app, s)) messenger.showSnackBar(SnackBar(content: Text(s.timeUp)));
  }

  Future<bool> _submit(AppController app, S s) async {
    if (_submitting) return false;
    setState(() => _submitting = true);
    _clock.stop();
    _ticker?.cancel();
    _ticker = null;
    try {
      await app.progress.saveElapsed(widget.attemptId, _elapsed);
      await app.progress.submitAttempt(widget.attemptId, app.content);
    } catch (e) {
      debugPrint('Could not submit attempt: $e');
      if (!mounted) return false;
      setState(() => _submitting = false);
      _resumeClock();
      await showDialog<void>(
        context: context,
        builder: (context) => AlertDialog(
          content: Text(s.submitFailed),
          actions: [FilledButton(onPressed: () => Navigator.pop(context), child: Text(s.ok))],
        ),
      );
      return false;
    }
    app.progressChanged();
    if (mounted) ResultScreen.replace(context, widget.attemptId, justSubmitted: true);
    return true;
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

  /// Practice shows the answer as soon as one is chosen; a mock test keeps
  /// answers hidden until it is submitted.
  bool get _instantFeedback => _attempt?.mode == AttemptMode.practice;

  void _toggleExplanation(Question question) {
    if (question.explanation.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(S.of(context).noExplanation)));
      return;
    }
    setState(() => _showExplanation = !_showExplanation);
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
    final selected = _selected[question.id];
    final revealed = _instantFeedback && selected != null;
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, _) {
        if (!didPop) _confirmLeave();
      },
      child: Scaffold(
        body: Column(
          children: [
            const BrandHeader(showAbout: false, showExams: false),
            Padding(
              padding: const EdgeInsets.fromLTRB(4, 8, 4, 0),
              child: Row(
                children: [
                  IconButton(
                    tooltip: s.leave,
                    icon: const Icon(Icons.close, color: Colors.white),
                    onPressed: _confirmLeave,
                  ),
                  Container(width: 5, height: 26, color: AppColors.sage),
                  const SizedBox(width: 8),
                  Expanded(
                    child: Text(attemptTitle(context, attempt),
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                        style: const TextStyle(color: Colors.white, fontSize: 20, fontWeight: FontWeight.w700)),
                  ),
                  if (_remaining case final remaining?) _CountdownChip(remaining: remaining, label: s.timeLeft),
                  const LanguageButton(),
                  IconButton(
                    tooltip: s.allQuestions,
                    icon: const Icon(Icons.grid_view, color: Colors.white),
                    onPressed: _showQuestionGrid,
                  ),
                ],
              ),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16),
              child: Row(
                children: [
                  Text(s.questionXofY(_index + 1, _questions.length),
                      style: const TextStyle(color: Colors.white70, fontSize: 13)),
                  const SizedBox(width: 12),
                  Expanded(
                    child: LinearProgressIndicator(
                      value: _answeredCount / _questions.length,
                      color: AppColors.mint,
                      backgroundColor: Colors.white24,
                      borderRadius: BorderRadius.circular(4),
                    ),
                  ),
                ],
              ),
            ),
            Expanded(
              child: SingleChildScrollView(
                key: ValueKey(question.id),
                padding: const EdgeInsets.fromLTRB(16, 12, 16, 16),
                child: QuestionView(
                  question: question,
                  heading: 'Q${_index + 1}',
                  inlineHeading: true,
                  selectedOptionId: selected,
                  correctOptionId: revealed ? question.correctOptionId : null,
                  showExplanation: revealed && _showExplanation,
                  onSelect: _submitting || revealed ? null : _select,
                ),
              ),
            ),
          ],
        ),
        bottomNavigationBar: SafeArea(
          child: Padding(
            padding: const EdgeInsets.fromLTRB(16, 8, 16, 12),
            child: Row(
              children: [
                if (_index > 0) ...[
                  IconButton.filled(
                    tooltip: s.previous,
                    style: IconButton.styleFrom(backgroundColor: AppColors.mint, foregroundColor: AppColors.deepTeal),
                    onPressed: () => _goTo(_index - 1),
                    icon: const Icon(Icons.chevron_left),
                  ),
                  const SizedBox(width: 8),
                ],
                if (_instantFeedback) ...[
                  Expanded(
                    child: PillButton(
                      label: s.explanation,
                      onPressed: revealed ? () => _toggleExplanation(question) : null,
                    ),
                  ),
                  const SizedBox(width: 12),
                ],
                Expanded(
                  child: isLast
                      ? PillButton(label: s.submit, onPressed: _submitting ? null : _confirmSubmit)
                      : PillButton(label: selected == null ? s.skip : s.nextArrows, onPressed: () => _goTo(_index + 1)),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _CountdownChip extends StatelessWidget {
  const _CountdownChip({required this.remaining, required this.label});

  static const _warnBelow = Duration(minutes: 5);

  final Duration remaining;
  final String label;

  @override
  Widget build(BuildContext context) {
    final scheme = Theme.of(context).colorScheme;
    final warn = remaining < _warnBelow;
    final color = warn ? scheme.onErrorContainer : scheme.onSecondaryContainer;
    return Semantics(
      label: label,
      child: Container(
        margin: const EdgeInsets.symmetric(vertical: 10),
        padding: const EdgeInsets.symmetric(horizontal: 8),
        decoration: BoxDecoration(
          color: warn ? scheme.errorContainer : scheme.secondaryContainer,
          borderRadius: BorderRadius.circular(8),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(Icons.timer_outlined, size: 16, color: color),
            const SizedBox(width: 4),
            Text(
              formatClock(remaining.isNegative ? Duration.zero : remaining),
              style: TextStyle(color: color, fontWeight: FontWeight.bold, fontFeatures: const [FontFeature.tabularFigures()]),
            ),
          ],
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
