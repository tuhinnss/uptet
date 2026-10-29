import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../widgets/brand.dart';
import '../widgets/common.dart';
import 'practice_screen.dart';
import 'quiz_launcher.dart';

/// One subject: practise a topic, or take a full paper that includes the subject.
class SubjectScreen extends StatelessWidget {
  const SubjectScreen({super.key, required this.subjectId});

  final String subjectId;

  static Future<void> open(BuildContext context, String subjectId) =>
      Navigator.of(context).push(MaterialPageRoute<void>(builder: (_) => SubjectScreen(subjectId: subjectId)));

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final content = app.content;
    final subject = content.subject(subjectId);
    if (subject == null) {
      return BrandPage(children: [EmptyState(icon: Icons.error_outline, title: s.noSubjects)]);
    }
    final topics = content.topicsFor(subjectId);
    final papers = [
      for (final paper in content.papers)
        if (content.questionsForPaper(paper.id).any((q) => q.subjectId == subjectId)) paper,
    ];
    return BrandPage(
      children: [
        SectionTitle(subject.name.resolve(app.language).text, back: true),
        ExpandableBrandCard(
          icon: const Icon(Icons.description_outlined),
          title: s.topicWiseQuestions,
          subtitle: s.questionsCount(content.questionCountForSubject(subjectId)),
          initiallyExpanded: true,
          children: [
            if (topics.isEmpty)
              Text(s.noTopicsYet, style: const TextStyle(color: Colors.white))
            else
              for (final topic in topics)
                Builder(builder: (context) {
                  final count = content.questionsForTopic(topic.id).length;
                  return InnerCard(
                    icon: const Icon(Icons.edit_note),
                    title: topic.name.resolve(app.language).text,
                    subtitle: count > 0 ? s.questionsCount(count) : s.noTopicQuestions,
                    enabled: count > 0,
                    onTap: () => startOrResumeTopic(context, topic),
                  );
                }),
          ],
        ),
        ExpandableBrandCard(
          icon: const Icon(Icons.description_outlined),
          title: s.fullPracticeSet,
          subtitle: s.subjectPapersSubtitle,
          children: [
            if (papers.isEmpty)
              Text(s.noPracticeSets, style: const TextStyle(color: Colors.white))
            else
              for (final paper in papers) PaperInnerCard(paper: paper),
          ],
        ),
      ],
    );
  }
}
