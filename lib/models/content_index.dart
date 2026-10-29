import 'content.dart';

/// In-memory view of the installed content, loaded once at startup.
///
/// Retired content (removed from a newer pack) stays reachable by ID so past
/// attempts can still be shown, but is excluded from new tests.
class ContentIndex {
  ContentIndex({
    required this.contentVersion,
    required this.releaseReady,
    required List<Subject> subjects,
    required List<Topic> topics,
    required List<Paper> papers,
    required List<Question> questions,
    required Set<String> activeSubjectIds,
    required Set<String> activeTopicIds,
    required Set<String> activePaperIds,
    required Set<String> activeQuestionIds,
  })  : _subjects = {for (final s in subjects) s.id: s},
        _topics = {for (final t in topics) t.id: t},
        _papers = {for (final p in papers) p.id: p},
        _questions = {for (final q in questions) q.id: q},
        subjects = subjects.where((s) => activeSubjectIds.contains(s.id)).toList()
          ..sort((a, b) => a.sortOrder.compareTo(b.sortOrder)),
        papers = papers.where((p) => activePaperIds.contains(p.id)).toList()
          ..sort((a, b) => a.sortOrder.compareTo(b.sortOrder)),
        _activeTopicIds = activeTopicIds,
        _activeQuestionIds = activeQuestionIds;

  final String contentVersion;
  final bool releaseReady;

  /// Active subjects and papers in display order.
  final List<Subject> subjects;
  final List<Paper> papers;

  final Map<String, Subject> _subjects;
  final Map<String, Topic> _topics;
  final Map<String, Paper> _papers;
  final Map<String, Question> _questions;
  final Set<String> _activeTopicIds;
  final Set<String> _activeQuestionIds;

  Subject? subject(String id) => _subjects[id];
  Topic? topic(String id) => _topics[id];
  Paper? paper(String id) => _papers[id];
  Question? question(String id) => _questions[id];

  List<Topic> topicsFor(String subjectId) => _topics.values
      .where((t) => t.subjectId == subjectId && _activeTopicIds.contains(t.id))
      .toList()
    ..sort((a, b) => a.sortOrder.compareTo(b.sortOrder));

  /// Active questions of a paper in exam order.
  List<Question> questionsForPaper(String paperId) {
    final paper = _papers[paperId];
    if (paper == null) return const [];
    return [
      for (final id in paper.questionIds)
        if (_activeQuestionIds.contains(id) && _questions[id] != null) _questions[id]!,
    ];
  }

  /// Active questions of a topic in content order, including paper questions.
  /// With [exam], only questions from that exam's papers.
  List<Question> questionsForTopic(String topicId, {Exam? exam}) => _questions.values
      .where((q) =>
          q.topicId == topicId &&
          _activeQuestionIds.contains(q.id) &&
          (exam == null || _questionIdsOf(exam).contains(q.id)))
      .toList()
    ..sort((a, b) => a.sortOrder.compareTo(b.sortOrder));

  int questionCountForSubject(String subjectId, {Exam? exam}) => topicsFor(subjectId)
      .fold(0, (sum, topic) => sum + questionsForTopic(topic.id, exam: exam).length);

  /// Active subjects that have questions from [exam]'s papers.
  List<Subject> subjectsFor(Exam exam) =>
      subjects.where((s) => questionCountForSubject(s.id, exam: exam) > 0).toList();

  final Map<Exam, Set<String>> _examQuestionIds = {};

  Set<String> _questionIdsOf(Exam exam) =>
      _examQuestionIds[exam] ??= {for (final p in papers) if (p.exam == exam) ...p.questionIds};

  /// Languages the paper's active questions are fully available in.
  Set<AppLanguage> paperLanguages(String paperId) =>
      paperLanguagesOf(questionsForPaper(paperId), (subjectId) => _subjects[subjectId]?.language);

  /// Papers of [exam] at [level] in display order.
  List<Paper> papersFor(Exam? exam, ExamLevel? level) =>
      papers.where((p) => p.exam == exam && p.level == level).toList();
}
