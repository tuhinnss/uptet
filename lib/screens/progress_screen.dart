import 'package:flutter/material.dart';

import '../app_state.dart';
import '../config.dart';
import '../l10n/strings.dart';
import '../repositories/progress_repository.dart';
import '../services/progress_calculator.dart';
import '../widgets/async_loader.dart';
import '../widgets/common.dart';
import '../widgets/settings_sheet.dart';
import 'quiz_launcher.dart';
import 'result_screen.dart';

class ProgressScreen extends StatelessWidget {
  const ProgressScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    return Scaffold(
      appBar: AppBar(title: Text(s.myProgress), actions: const [LanguageButton()]),
      body: AsyncLoader<ProgressReport>(
        load: (app) => app.progress.progressReport(),
        builder: (context, report) => report.testsCompleted == 0
            ? ListView(
                padding: const EdgeInsets.all(16),
                children: [
                  EmptyState(icon: Icons.insights_outlined, title: s.progressEmptyTitle, message: s.progressEmptyBody),
                  const _AboutData(),
                ],
              )
            : _Report(report: report),
      ),
    );
  }
}

class _Report extends StatelessWidget {
  const _Report({required this.report});

  final ProgressReport report;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final theme = Theme.of(context);
    final weak = weakTopics(report.topics);
    final weakIds = {for (final w in weak) w.topicId};
    final anyJudged = report.topics.any((t) => t.answered >= AppConfig.weakTopicMinAnswered);
    String topicName(String id) => app.content.topic(id)?.name.resolve(app.language).text ?? id;

    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        StatGrid(tiles: [
          StatTile(label: s.testsCompleted, value: '${report.testsCompleted}'),
          StatTile(label: s.accuracy, value: formatPercent(report.accuracyPercent)),
          StatTile(label: s.questionsAttempted, value: '${report.attempted}'),
          StatTile(label: s.answeredCorrectly, value: '${report.correct}'),
          StatTile(label: s.answeredIncorrectly, value: '${report.incorrect}'),
          StatTile(label: s.skipped, value: '${report.unanswered}'),
          StatTile(label: s.awaitingRevision, value: '${report.revision.active}'),
        ]),
        const SizedBox(height: 8),
        Text(s.accuracyNote, style: theme.textTheme.bodySmall),
        SectionHeader(s.topicsToPractise),
        if (weak.isEmpty)
          Text(anyJudged ? s.noWeakTopics : s.notEnoughData(AppConfig.weakTopicMinAnswered))
        else
          for (final w in weak) _WeakTopicCard(performance: w, name: topicName(w.topicId)),
        if (report.topics.isNotEmpty) ...[
          SectionHeader(s.topicPerformance),
          for (final t in report.topics)
            ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 4),
              title: Text(topicName(t.topicId)),
              subtitle: Text([
                s.topicStats(t.correct, t.answered),
                if (weakIds.contains(t.topicId)) s.needsPractice,
              ].join(' · ')),
              trailing: Text(formatPercent(t.accuracyPercent), style: theme.textTheme.titleMedium),
            ),
        ],
        SectionHeader(s.history),
        for (final attempt in report.attempts)
          Card(
            child: ListTile(
              title: Text(attemptTitle(context, attempt)),
              subtitle: Text(attemptSubtitle(context, attempt)),
              trailing: Text(attemptScore(attempt), style: theme.textTheme.titleSmall),
              onTap: () => ResultScreen.open(context, attempt.id),
            ),
          ),
        const _AboutData(),
      ],
    );
  }
}

class _WeakTopicCard extends StatelessWidget {
  const _WeakTopicCard({required this.performance, required this.name});

  final TopicPerformance performance;
  final String name;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final topic = app.content.topic(performance.topicId);
    final canPractise = topic != null && app.content.questionsForTopic(topic.id).isNotEmpty;
    return Card(
      child: ListTile(
        leading: const Icon(Icons.flag_outlined),
        title: Text(name),
        subtitle: Text('${s.topicStats(performance.correct, performance.answered)} · ${formatPercent(performance.accuracyPercent)}'),
        trailing: canPractise
            ? TextButton(onPressed: () => startOrResumeTopic(context, topic), child: Text(s.navPractice))
            : null,
      ),
    );
  }
}

class _AboutData extends StatelessWidget {
  const _AboutData();

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final theme = Theme.of(context);
    return Padding(
      padding: const EdgeInsets.only(top: 24),
      child: Card(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(children: [
                const Icon(Icons.lock_outline, size: 20),
                const SizedBox(width: 8),
                Text(s.aboutDataTitle, style: theme.textTheme.titleSmall),
              ]),
              const SizedBox(height: 8),
              Text(s.aboutDataBody, style: theme.textTheme.bodySmall?.copyWith(height: 1.5)),
            ],
          ),
        ),
      ),
    );
  }
}
