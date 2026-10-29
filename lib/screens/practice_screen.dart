import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/content.dart';
import '../repositories/progress_repository.dart';
import '../widgets/async_loader.dart';
import '../widgets/brand.dart';
import '../widgets/common.dart';
import '../widgets/subject_icon.dart';
import 'paper_detail_screen.dart';
import 'review_screen.dart';
import 'revision_list_screen.dart';
import 'subject_screen.dart';

class PracticeScreen extends StatelessWidget {
  const PracticeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    // Papers without an exam and level are practice sets, not previous papers.
    final sets = app.content.papers.where((p) => p.exam == null || p.level == null).toList();
    final subjects = app.content.subjectsFor(app.exam);
    return BrandPage(
      children: [
        SectionTitle(s.practiceAndRevision),
        ExpandableBrandCard(
          icon: const Icon(Icons.description_outlined),
          title: s.topicWiseQuestions,
          subtitle: s.topicWiseSubtitle,
          children: [
            if (subjects.isEmpty)
              Text(s.noExamSubjects, style: const TextStyle(color: Colors.white))
            else
              for (final subject in subjects)
                InnerCard(
                  icon: subjectIcon(subject),
                  title: subject.name.resolve(app.language).text,
                  onTap: () => SubjectScreen.open(context, subject.id),
                ),
          ],
        ),
        ExpandableBrandCard(
          icon: const Icon(Icons.description_outlined),
          title: s.fullPracticeSet,
          subtitle: s.fullPracticeSubtitle,
          children: [
            if (sets.isEmpty)
              Text(s.noPracticeSets, style: const TextStyle(color: Colors.white))
            else
              for (final paper in sets) PaperInnerCard(paper: paper),
          ],
        ),
        AsyncLoader<RevisionOverview>(
          load: (app) => app.progress.revisionOverview(),
          builder: (context, overview) => _RevisionCard(overview: overview),
        ),
      ],
    );
  }
}

/// A practice set or paper inside an expanded card.
class PaperInnerCard extends StatelessWidget {
  const PaperInnerCard({super.key, required this.paper});

  final Paper paper;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    return InnerCard(
      icon: const Icon(Icons.edit_note),
      title: paper.title.resolve(app.language).text,
      subtitle: s.questionsCount(app.content.questionsForPaper(paper.id).length),
      onTap: () => PaperDetailScreen.open(context, paper.id),
    );
  }
}

/// Spaced revision of questions answered wrongly in tests.
class _RevisionCard extends StatelessWidget {
  const _RevisionCard({required this.overview});

  final RevisionOverview overview;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final hasAny = overview.active + overview.mastered > 0;
    final String message;
    if (overview.due > 0) {
      message = s.dueTodayCount(overview.due);
    } else if (overview.nextDueAt case final next?) {
      message = '${s.noneDueToday} ${s.nextReviewOn(formatDate(context, next))}';
    } else {
      message = s.revisionEmptyHint;
    }
    return BrandCard(
      icon: Image.asset(BrandAssets.revision, width: 52, height: 52),
      title: s.reviseMistakes,
      subtitle: message,
      onTap: overview.due > 0
          ? () => ReviewScreen.open(context)
          : hasAny
              ? () => RevisionListScreen.open(context)
              : null,
    );
  }
}
