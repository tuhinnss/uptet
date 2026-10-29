import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/content.dart';
import '../theme.dart';
import '../widgets/brand.dart';
import '../widgets/subject_icon.dart';
import 'quiz_launcher.dart';

/// The pattern of the exam chosen in the header, then the subjects and topics
/// this app covers for it.
class SyllabusScreen extends StatelessWidget {
  const SyllabusScreen({super.key});

  static Future<void> open(BuildContext context) =>
      Navigator.of(context).push(MaterialPageRoute<void>(builder: (_) => const SyllabusScreen()));

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final exam = app.exam;
    return BrandPage(
      children: [
        SectionTitle(s.syllabus, back: true),
        SectionTitle(s.examPattern(exam), size: 22),
        if (exam == Exam.supertet)
          _PatternCard(
            title: s.superTetPaper,
            rows: [
              (s.sectionHindi, 20),
              (s.sectionSanskrit, 10),
              (s.sectionEnglish, 10),
              (s.sectionGk, 10),
              (s.sectionCdp, 20),
              (s.sectionScience, 10),
              (s.sectionMaths, 20),
              (s.sectionCurrentAffairs, 30),
              (s.sectionLifeSkills, 10),
              (s.sectionReasoning, 5),
              (s.sectionIct, 5),
            ],
          )
        else ...[
          // UPTET and CTET share the two-paper pattern.
          _PatternCard(
            title: s.paperOne,
            rows: [
              (s.sectionCdp, 30),
              (s.sectionLanguageOne, 30),
              (s.sectionLanguageTwo, 30),
              (s.sectionMaths, 30),
              (s.sectionEvs, 30),
            ],
          ),
          _PatternCard(
            title: s.paperTwo,
            rows: [
              (s.sectionCdp, 30),
              (s.sectionLanguageOne, 30),
              (s.sectionLanguageTwo, 30),
              (s.sectionMathsScienceOrSst, 60),
            ],
          ),
        ],
        Text(
          switch (exam) {
            Exam.uptet => s.patternRules,
            Exam.supertet => s.superTetPatternRules,
            Exam.ctet => s.ctetPatternRules,
          },
          style: const TextStyle(color: Colors.white, fontSize: 15, height: 1.5),
        ),
        const SizedBox(height: 8),
        Text(s.patternNote, style: const TextStyle(color: Colors.white70, fontSize: 13, height: 1.4)),
        const SizedBox(height: 24),
        SectionTitle(s.topicsInApp, size: 22),
        for (final subject in app.content.subjectsFor(exam))
          ExpandableBrandCard(
            icon: subjectIcon(subject),
            title: subject.name.resolve(app.language).text,
            subtitle: s.questionsCount(app.content.questionCountForSubject(subject.id, exam: exam)),
            children: [
              for (final topic in app.content.topicsFor(subject.id))
                Builder(builder: (context) {
                  final count = app.content.questionsForTopic(topic.id, exam: exam).length;
                  return InnerCard(
                    title: topic.name.resolve(app.language).text,
                    subtitle: count > 0 ? s.questionsCount(count) : s.noTopicQuestions,
                    enabled: count > 0,
                    onTap: () => startOrResumeTopic(context, topic),
                  );
                }),
            ],
          ),
      ],
    );
  }
}

class _PatternCard extends StatelessWidget {
  const _PatternCard({required this.title, required this.rows});

  final String title;
  final List<(String, int)> rows;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    const text = TextStyle(color: Colors.white, fontSize: 15, height: 1.35);
    return Container(
      margin: const EdgeInsets.only(bottom: 16),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(color: AppColors.sage, borderRadius: BorderRadius.circular(24)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Text(title, style: const TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.w700)),
          const SizedBox(height: 8),
          for (final (name, count) in rows)
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 4),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Expanded(child: Text(name, style: text)),
                  const SizedBox(width: 12),
                  Text(s.questionsShort(count), style: text.copyWith(fontWeight: FontWeight.w600)),
                ],
              ),
            ),
          const Divider(color: Colors.white54),
          Text(s.patternTotals, style: text.copyWith(fontWeight: FontWeight.w600)),
        ],
      ),
    );
  }
}
