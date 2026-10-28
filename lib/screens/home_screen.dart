import 'package:flutter/material.dart';

import '../app.dart';
import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/attempt.dart';
import '../repositories/progress_repository.dart';
import '../widgets/async_loader.dart';
import '../widgets/common.dart';
import '../widgets/settings_sheet.dart';
import 'quiz_screen.dart';
import 'review_screen.dart';

class _HomeData {
  const _HomeData(this.resume, this.revision);

  final Attempt? resume;
  final RevisionOverview revision;
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key, required this.onNavigate});

  final ValueChanged<MainTab> onNavigate;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final theme = Theme.of(context);
    return Scaffold(
      appBar: AppBar(title: Text(s.appName), actions: const [LanguageButton()]),
      body: AsyncLoader<_HomeData>(
        load: (app) async => _HomeData(await app.progress.latestInProgress(), await app.progress.revisionOverview()),
        builder: (context, data) => ListView(
          padding: const EdgeInsets.all(16),
          children: [
            Text(s.welcomeTitle, style: theme.textTheme.headlineSmall),
            const SizedBox(height: 4),
            Text(s.welcomeMessage, style: theme.textTheme.bodyLarge),
            if (app.contentWarning != null) ...[
              const SizedBox(height: 16),
              NoticeBanner(icon: Icons.warning_amber, text: s.contentUpdateFailed),
            ],
            if (!app.content.releaseReady) ...[
              const SizedBox(height: 16),
              NoticeBanner(icon: Icons.info_outline, text: s.pilotNotice),
            ],
            if (data.resume case final attempt?) ...[
              const SizedBox(height: 16),
              _ResumeCard(attempt: attempt),
            ],
            const SizedBox(height: 16),
            _RevisionCard(overview: data.revision),
            SectionHeader(s.startStudying),
            _NavCard(
              icon: Icons.description_outlined,
              title: s.previousPapers,
              subtitle: s.papersSubtitle,
              onTap: () => onNavigate(MainTab.papers),
            ),
            _NavCard(
              icon: Icons.edit_note_outlined,
              title: s.practiceAndRevision,
              subtitle: s.practiceSubtitle,
              onTap: () => onNavigate(MainTab.practice),
            ),
            _NavCard(
              icon: Icons.insights_outlined,
              title: s.myProgress,
              subtitle: s.progressSubtitle,
              onTap: () => onNavigate(MainTab.progress),
            ),
          ],
        ),
      ),
    );
  }
}

class _ResumeCard extends StatelessWidget {
  const _ResumeCard({required this.attempt});

  final Attempt attempt;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final theme = Theme.of(context);
    return Card(
      color: theme.colorScheme.primaryContainer,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(s.continueWhereLeft, style: theme.textTheme.labelLarge),
            const SizedBox(height: 6),
            Text(attemptTitle(context, attempt), style: theme.textTheme.titleMedium),
            Text(s.questionXofY(attempt.currentIndex + 1, attempt.totalQuestions)),
            const SizedBox(height: 12),
            FilledButton.icon(
              onPressed: () => QuizScreen.open(context, attempt.id),
              icon: const Icon(Icons.play_arrow),
              label: Text(s.resume),
            ),
          ],
        ),
      ),
    );
  }
}

class _RevisionCard extends StatelessWidget {
  const _RevisionCard({required this.overview});

  final RevisionOverview overview;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final theme = Theme.of(context);
    final nextDue = overview.nextDueAt;
    final String message;
    if (overview.due > 0) {
      message = s.dueTodayCount(overview.due);
    } else if (nextDue != null) {
      message = '${s.noneDueToday} ${s.nextReviewOn(formatDate(context, nextDue))}';
    } else {
      message = s.revisionEmptyHint;
    }
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
            Text(message),
            if (overview.due > 0) ...[
              const SizedBox(height: 12),
              FilledButton(onPressed: () => ReviewScreen.open(context), child: Text(s.reviseNow)),
            ],
          ],
        ),
      ),
    );
  }
}

class _NavCard extends StatelessWidget {
  const _NavCard({required this.icon, required this.title, required this.subtitle, required this.onTap});

  final IconData icon;
  final String title;
  final String subtitle;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) => Card(
        child: ListTile(
          leading: Icon(icon),
          title: Text(title),
          subtitle: Text(subtitle),
          trailing: const Icon(Icons.chevron_right),
          onTap: onTap,
        ),
      );
}
