import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/content.dart';
import '../widgets/brand.dart';
import '../widgets/common.dart';
import 'paper_detail_screen.dart';

/// Official papers of the exam chosen in the header, by year, newest first. A
/// year with several papers opens in place to list them by level.
class PapersScreen extends StatelessWidget {
  const PapersScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final groups = officialPaperGroups(app.content.papers.where((p) => p.exam == app.exam).toList());
    return BrandPage(
      children: [
        SectionTitle(s.examPapers(app.exam)),
        if (groups.isEmpty)
          EmptyState(icon: Icons.description_outlined, title: s.noPapers, message: s.noPapersHint)
        else
          for (final group in groups)
            if (group.papers.length == 1)
              BrandCard(
                icon: const Icon(Icons.description_outlined),
                title: group.title(s),
                subtitle: paperLabel(s, app.language, group.papers.single),
                onTap: () => PaperDetailScreen.open(context, group.papers.single.id),
              )
            else
              ExpandableBrandCard(
                icon: const Icon(Icons.description_outlined),
                title: group.title(s),
                subtitle: s.paperCount(group.papers.length),
                children: [
                  for (final paper in group.papers)
                    InnerCard(
                      icon: const Icon(Icons.description_outlined),
                      title: s.levelWord(paper.level!),
                      subtitle: [s.levelClasses(paper.level!), paperPart(paper, app.language)].nonNulls.join(' · '),
                      singleLine: true,
                      onTap: () => PaperDetailScreen.open(context, paper.id),
                    ),
                ],
              ),
      ],
    );
  }
}

class PaperGroup {
  const PaperGroup(this.exam, this.year, this.papers);

  final Exam exam;
  final int? year;
  final List<Paper> papers;

  String title(S s) => year == null ? s.examName(exam) : '${s.examName(exam)} $year';
}

/// Official papers by exam, then year (newest first); Primary before Junior within a year.
List<PaperGroup> officialPaperGroups(List<Paper> papers) {
  final groups = <(Exam, int?), List<Paper>>{};
  for (final paper in papers) {
    if (paper.exam == null || paper.level == null) continue;
    groups.putIfAbsent((paper.exam!, paper.year), () => []).add(paper);
  }
  final keys = groups.keys.toList()
    ..sort((a, b) => a.$1 != b.$1 ? a.$1.index.compareTo(b.$1.index) : (b.$2 ?? 0).compareTo(a.$2 ?? 0));
  return [
    for (final key in keys)
      PaperGroup(key.$1, key.$2, groups[key]!..sort((a, b) => a.level!.index.compareTo(b.level!.index))),
  ];
}

/// What tells papers of one year apart: the part of the title after exam and
/// level, such as "Social Studies".
String? paperPart(Paper paper, AppLanguage language) {
  final parts = paper.title.resolve(language).text.split(' · ');
  return parts.length > 2 ? parts.sublist(2).join(' · ') : null;
}

/// Level, and the distinguishing part when there is one.
String paperLabel(S s, AppLanguage language, Paper paper) {
  final part = paperPart(paper, language);
  return [
    if (paper.level != null) s.levelShort(paper.level!),
    if (part != null) part,
  ].join(' · ');
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
