import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/content.dart';
import '../repositories/progress_repository.dart';
import '../widgets/async_loader.dart';
import '../widgets/common.dart';
import '../widgets/settings_sheet.dart';
import 'quiz_launcher.dart';
import 'review_screen.dart';
import 'revision_list_screen.dart';

class PracticeScreen extends StatelessWidget {
  const PracticeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    return Scaffold(
      appBar: AppBar(title: Text(s.practiceAndRevision), actions: const [LanguageButton()]),
      body: AsyncLoader<RevisionOverview>(
        load: (app) => app.progress.revisionOverview(),
        builder: (context, overview) => ListView(
          padding: const EdgeInsets.all(16),
          children: [
            _RevisionSummary(overview: overview),
            SectionHeader(s.topicPractice),
            if (app.content.subjects.isEmpty)
              EmptyState(icon: Icons.menu_book_outlined, title: s.noSubjects)
            else
              for (final subject in app.content.subjects) _SubjectCard(subject: subject),
          ],
        ),
      ),
    );
  }
}

class _RevisionSummary extends StatelessWidget {
  const _RevisionSummary({required this.overview});

  final RevisionOverview overview;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final theme = Theme.of(context);
    final hasAny = overview.active + overview.mastered > 0;
    return Card(
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(children: [
              const Icon(Icons.replay),
              const SizedBox(width: 8),
              Text(s.revision, style: theme.textTheme.titleMedium),
            ]),
            const SizedBox(height: 8),
            Text(
              overview.due > 0 ? s.dueTodayCount(overview.due) : (hasAny ? s.noneDueToday : s.revisionEmptyHint),
              style: theme.textTheme.bodyLarge,
            ),
            if (hasAny) ...[
              const SizedBox(height: 8),
              Wrap(spacing: 6, runSpacing: 6, children: [
                InfoChip(icon: Icons.schedule, label: s.upcomingCount(overview.upcoming)),
                InfoChip(icon: Icons.check, label: s.masteredCount(overview.mastered)),
              ]),
            ],
            const SizedBox(height: 8),
            Text(s.revisionSchedule, style: theme.textTheme.bodySmall),
            const SizedBox(height: 12),
            Wrap(spacing: 8, runSpacing: 8, children: [
              if (overview.due > 0) FilledButton(onPressed: () => ReviewScreen.open(context), child: Text(s.reviseNow)),
              if (hasAny) OutlinedButton(onPressed: () => RevisionListScreen.open(context), child: Text(s.revisionList)),
            ]),
          ],
        ),
      ),
    );
  }
}

class _SubjectCard extends StatelessWidget {
  const _SubjectCard({required this.subject});

  final Subject subject;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final topics = app.content.topicsFor(subject.id);
    return Card(
      clipBehavior: Clip.antiAlias,
      child: ExpansionTile(
        shape: const Border(),
        collapsedShape: const Border(),
        title: Text(subject.name.resolve(app.language).text),
        subtitle: Text(s.questionsCount(app.content.questionCountForSubject(subject.id))),
        children: [
          for (final topic in topics)
            Builder(builder: (context) {
              final count = app.content.questionsForTopic(topic.id).length;
              return ListTile(
                enabled: count > 0,
                contentPadding: const EdgeInsets.only(left: 32, right: 16),
                title: Text(topic.name.resolve(app.language).text),
                subtitle: Text(count > 0 ? s.questionsCount(count) : s.noTopicQuestions),
                trailing: count > 0 ? const Icon(Icons.play_circle_outline) : null,
                onTap: () => startOrResumeTopic(context, topic),
              );
            }),
        ],
      ),
    );
  }
}
