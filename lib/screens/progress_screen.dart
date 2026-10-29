import 'package:flutter/material.dart';

import '../app_state.dart';
import '../config.dart';
import '../l10n/strings.dart';
import '../repositories/progress_repository.dart';
import '../services/progress_calculator.dart';
import '../services/study_activity.dart';
import '../theme.dart';
import '../widgets/activity_heat_map.dart';
import '../widgets/async_loader.dart';
import '../widgets/brand.dart';
import '../widgets/common.dart';
import 'quiz_launcher.dart';
import 'result_screen.dart';

class ProgressScreen extends StatelessWidget {
  const ProgressScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          const BrandHeader(),
          Expanded(
            child: AsyncLoader<ProgressReport>(
              load: (app) => app.progress.progressReport(),
              builder: (context, report) => _Report(report: report, today: DateTime.now()),
            ),
          ),
        ],
      ),
    );
  }
}

class _Report extends StatelessWidget {
  const _Report({required this.report, required this.today});

  final ProgressReport report;
  final DateTime today;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final content = app.content;
    final totalQuestions = content.subjects.fold(0, (sum, subject) => sum + content.questionCountForSubject(subject.id));
    final weak = weakTopics(report.topics);
    final anyJudged = report.topics.any((t) => t.answered >= AppConfig.weakTopicMinAnswered);
    String topicName(String id) => content.topic(id)?.name.resolve(app.language).text ?? id;

    return ListView(
      padding: const EdgeInsets.fromLTRB(16, 20, 16, 24),
      children: [
        SectionTitle(s.myProgress),
        ActivityHeatMap(days: report.studyDays, today: today),
        const SizedBox(height: 16),
        _StreakCard(streaks: streaksOf(report.studyDays, today), studiedToday: _studiedToday),
        const SizedBox(height: 16),
        LayoutBuilder(builder: (context, constraints) {
          final width = (constraints.maxWidth - 14) / 2;
          return Wrap(
            spacing: 14,
            runSpacing: 14,
            children: [
              for (final box in [
                StatBox(
                  value: '${report.papersCompleted}',
                  note: s.outOf(content.papers.length),
                  label: s.papersCompletedLabel,
                ),
                StatBox(value: formatPercent(report.accuracyPercent), label: s.accuracy),
                StatBox(
                  value: '${report.distinctQuestionsAttempted}',
                  note: s.outOf(totalQuestions),
                  label: s.questionsAttempted,
                ),
                StatBox(value: s.studyTime(timeThisWeek(report.studyDays, today)), label: s.weeklyTime),
              ])
                SizedBox(width: width, child: box),
            ],
          );
        }),
        const SizedBox(height: 14),
        _QuestionReport(report: report),
        const SizedBox(height: 4),
        Text(s.accuracyNote, style: const TextStyle(color: Colors.white70, fontSize: 13)),
        if (report.testsCompleted > 0) ...[
          const SizedBox(height: 24),
          SectionTitle(s.topicsToPractise, size: 22),
          if (weak.isEmpty)
            Text(anyJudged ? s.noWeakTopics : s.notEnoughData(AppConfig.weakTopicMinAnswered),
                style: const TextStyle(color: Colors.white))
          else
            for (final w in weak)
              Builder(builder: (context) {
                final topic = content.topic(w.topicId);
                final canPractise = topic != null && content.questionsForTopic(topic.id).isNotEmpty;
                return InnerCard(
                  icon: const Icon(Icons.flag_outlined),
                  title: topicName(w.topicId),
                  subtitle: '${s.topicStats(w.correct, w.answered)} · ${formatPercent(w.accuracyPercent)}',
                  enabled: canPractise,
                  onTap: canPractise ? () => startOrResumeTopic(context, topic) : null,
                );
              }),
          const SizedBox(height: 16),
          SectionTitle(s.history, size: 22),
          for (final attempt in report.attempts)
            InnerCard(
              icon: const Icon(Icons.assignment_turned_in_outlined),
              title: attemptTitle(context, attempt),
              subtitle: '${attemptScore(attempt)} · ${attemptSubtitle(context, attempt)}',
              onTap: () => ResultScreen.open(context, attempt.id),
            ),
        ] else ...[
          const SizedBox(height: 16),
          Text(s.progressEmptyBody, style: const TextStyle(color: Colors.white, fontSize: 15)),
        ],
      ],
    );
  }

  bool get _studiedToday => report.studyDays.any((d) => d.isActive && dateOnly(d.day) == dateOnly(today));
}

class _StreakCard extends StatelessWidget {
  const _StreakCard({required this.streaks, required this.studiedToday});

  final Streaks streaks;
  final bool studiedToday;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final hint = streaks.current == 0 ? s.startStreak : (studiedToday ? null : s.keepStreak);
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(color: AppColors.mint, borderRadius: BorderRadius.circular(24)),
      child: Row(
        children: [
          Icon(Icons.local_fire_department,
              size: 44, color: streaks.current > 0 ? AppColors.sun : AppColors.accentTeal.withValues(alpha: 0.4)),
          const SizedBox(width: 10),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(s.dayStreak(streaks.current),
                    style: const TextStyle(color: AppColors.deepTeal, fontSize: 20, fontWeight: FontWeight.w700)),
                Text(s.bestStreak(streaks.best), style: const TextStyle(color: AppColors.accentTeal, fontSize: 14)),
                if (hint != null) Text(hint, style: const TextStyle(color: AppColors.deepTeal, fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _QuestionReport extends StatelessWidget {
  const _QuestionReport({required this.report});

  final ProgressReport report;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    Widget count(int value, String label, Color color, CrossAxisAlignment align) => Expanded(
          child: Column(
            crossAxisAlignment: align,
            children: [
              Text('$value', style: TextStyle(color: color, fontSize: 48, fontWeight: FontWeight.w700, height: 1.1)),
              Text(label, style: const TextStyle(color: Colors.white, fontSize: 17)),
            ],
          ),
        );
    return Container(
      padding: const EdgeInsets.fromLTRB(18, 12, 18, 14),
      decoration: BoxDecoration(color: AppColors.sage, borderRadius: BorderRadius.circular(24)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(s.questionReport, style: const TextStyle(color: Colors.white, fontSize: 20)),
          Row(
            children: [
              count(report.correct, s.correct, const Color(0xFFD9FBC8), CrossAxisAlignment.start),
              count(report.unanswered, s.skipped, Colors.white, CrossAxisAlignment.center),
              count(report.incorrect, s.incorrect, const Color(0xFFF7B9B9), CrossAxisAlignment.end),
            ],
          ),
        ],
      ),
    );
  }
}
