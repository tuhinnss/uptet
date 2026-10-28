import 'package:uptet_saathi/models/content.dart';

/// A minimal bilingual four-option question for tests.
Question question(
  String id, {
  String correct = 'A',
  String topicId = 't1',
  String subjectId = 's1',
  VerificationStatus status = VerificationStatus.verified,
}) =>
    Question(
      id: id,
      subjectId: subjectId,
      topicId: topicId,
      text: LocalizedText(en: 'Question $id', hi: 'प्रश्न $id'),
      options: [
        for (final o in ['A', 'B', 'C', 'D']) AnswerOption(id: o, text: LocalizedText(en: o, hi: o)),
      ],
      correctOptionId: correct,
      explanation: const LocalizedText(en: 'Because.', hi: 'क्योंकि।'),
      source: 'test',
      verificationStatus: status,
      sortOrder: 0,
    );

/// JSON for a small valid pack: one subject with two topics, three questions,
/// and a paper made of the first two questions.
Map<String, Object?> samplePackJson({String version = 'v1', List<String>? questionIds}) {
  final ids = questionIds ?? ['q1', 'q2', 'q3'];
  Map<String, Object?> q(String id, String topic) => {
        'id': id,
        'subject_id': 's1',
        'topic_id': topic,
        'text': {'en': 'Question $id', 'hi': 'प्रश्न $id'},
        'options': [
          for (final o in ['A', 'B', 'C', 'D'])
            {
              'id': o,
              'text': {'en': o, 'hi': o},
            },
        ],
        'correct_option_id': 'A',
        'explanation': {'en': 'Because.', 'hi': 'क्योंकि।'},
        'source': 'test',
        'verification_status': 'verified',
      };
  final paperIds = ids.where((id) => id != 'q3').toList();
  return {
    'schema_version': 1,
    'content_version': version,
    'release_ready': true,
    'subjects': [
      {
        'id': 's1',
        'name': {'en': 'Subject', 'hi': 'विषय'},
        'topics': [
          {
            'id': 't1',
            'name': {'en': 'Topic 1', 'hi': 'प्रकरण 1'},
          },
          {
            'id': 't2',
            'name': {'en': 'Topic 2', 'hi': 'प्रकरण 2'},
          },
        ],
      },
    ],
    'papers': [
      {
        'id': 'p1',
        'title': {'en': 'Paper', 'hi': 'प्रश्नपत्र'},
        'year': null,
        'paper_code': 'P1',
        'is_official_pyq': false,
        'distribution_cleared': true,
        'duration_minutes': 10,
        'marking': {'correct': 1},
        'pdf_asset': null,
        'source': 'test',
        'question_count': paperIds.length,
        'question_ids': paperIds,
      },
    ],
    'questions': [for (final id in ids) q(id, id == 'q3' ? 't2' : 't1')],
  };
}
