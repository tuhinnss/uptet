import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/content.dart';
import '../widgets/common.dart';
import '../widgets/settings_sheet.dart';
import 'paper_detail_screen.dart';

class PapersScreen extends StatelessWidget {
  const PapersScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final content = app.content;
    // Papers without an exam and level (practice sets) are listed last.
    final practice = content.papers.where((p) => p.exam == null || p.level == null).toList();
    return Scaffold(
      appBar: AppBar(title: Text(s.previousPapers), actions: const [LanguageButton()]),
      body: content.papers.isEmpty
          ? EmptyState(icon: Icons.description_outlined, title: s.noPapers, message: s.noPapersHint)
          : ListView(
              padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
              children: [
                for (final exam in Exam.values)
                  if (content.papers.any((p) => p.exam == exam && p.level != null)) ...[
                    SectionHeader(s.examPapers(exam)),
                    for (final level in ExamLevel.values)
                      if (content.papersFor(exam, level) case final papers when papers.isNotEmpty) ...[
                        _LevelHeader(s.levelName(level)),
                        for (final paper in papers) _PaperCard(paper: paper),
                      ],
                  ],
                if (practice.isNotEmpty) ...[
                  SectionHeader(s.practiceSets),
                  for (final paper in practice) _PaperCard(paper: paper),
                ],
              ],
            ),
    );
  }
}

class _LevelHeader extends StatelessWidget {
  const _LevelHeader(this.text);

  final String text;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return Padding(
      padding: const EdgeInsets.fromLTRB(4, 8, 4, 8),
      child: Text(text, style: theme.textTheme.labelLarge?.copyWith(color: theme.colorScheme.primary)),
    );
  }
}

class _PaperCard extends StatelessWidget {
  const _PaperCard({required this.paper});

  final Paper paper;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final theme = Theme.of(context);
    final languages = app.content.paperLanguages(paper.id);
    return Card(
      margin: const EdgeInsets.only(bottom: 8),
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: () => Navigator.of(context).push(
          MaterialPageRoute<void>(builder: (_) => PaperDetailScreen(paperId: paper.id)),
        ),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(paper.title.resolve(app.language).text, style: theme.textTheme.titleMedium),
              const SizedBox(height: 8),
              PaperBadge(paper: paper),
              const SizedBox(height: 8),
              Wrap(
                spacing: 6,
                runSpacing: 6,
                children: [
                  if (paper.year != null) InfoChip(icon: Icons.event, label: '${paper.year}'),
                  if (paper.paperCode != null) InfoChip(icon: Icons.tag, label: paper.paperCode!),
                  InfoChip(icon: Icons.quiz_outlined, label: s.questionsCount(app.content.questionsForPaper(paper.id).length)),
                  if (languages.isNotEmpty)
                    InfoChip(icon: Icons.translate, label: languages.map(s.languageName).join(' · ')),
                  if (paper.durationMinutes != null)
                    InfoChip(icon: Icons.timer_outlined, label: s.minutes(paper.durationMinutes!)),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

/// Makes clear whether a paper is a checked official paper or a practice set.
class PaperBadge extends StatelessWidget {
  const PaperBadge({super.key, required this.paper});

  final Paper paper;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    return paper.isOfficialPyq
        ? InfoChip(icon: Icons.verified_outlined, label: s.officialPaper)
        : InfoChip(icon: Icons.info_outline, label: s.practiceSetBadge);
  }
}
