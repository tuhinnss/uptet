import '../models/content.dart';

enum IssueSeverity { error, warning }

class ContentIssue {
  const ContentIssue(this.severity, this.message);

  final IssueSeverity severity;
  final String message;

  bool get isError => severity == IssueSeverity.error;

  @override
  String toString() => '${severity.name.toUpperCase()}: $message';
}

/// Cross-checks a parsed content pack. Errors block the pack from being
/// installed; warnings are for the content maintainer.
///
/// [assetExists] checks bundled file paths (PDFs) when the caller can see them.
List<ContentIssue> validateContentPack(ContentPack pack, {bool Function(String path)? assetExists}) {
  final issues = <ContentIssue>[];
  void error(String m) => issues.add(ContentIssue(IssueSeverity.error, m));
  void warn(String m) => issues.add(ContentIssue(IssueSeverity.warning, m));

  void checkUnique(Iterable<String> ids, String kind) {
    final seen = <String>{};
    for (final id in ids) {
      if (!seen.add(id)) error('Duplicate $kind ID "$id"');
    }
  }

  checkUnique(pack.subjects.map((s) => s.id), 'subject');
  checkUnique(pack.topics.map((t) => t.id), 'topic');
  checkUnique(pack.papers.map((p) => p.id), 'paper');
  checkUnique(pack.questions.map((q) => q.id), 'question');

  for (final s in pack.subjects) {
    if (s.name.isEmpty) error('Subject "${s.id}" has no name');
  }
  for (final t in pack.topics) {
    if (t.name.isEmpty) error('Topic "${t.id}" has no name');
  }

  final topicSubject = {for (final t in pack.topics) t.id: t.subjectId};
  final subjectLanguage = {for (final s in pack.subjects) s.id: s.language};
  final questionsById = {for (final q in pack.questions) q.id: q};

  for (final q in pack.questions) {
    final ctx = 'Question "${q.id}"';
    if (!topicSubject.containsKey(q.topicId)) {
      error('$ctx uses unknown topic "${q.topicId}"');
    } else if (topicSubject[q.topicId] != q.subjectId) {
      error('$ctx: topic "${q.topicId}" does not belong to subject "${q.subjectId}"');
    }
    if (q.text.isEmpty) error('$ctx has no question text');
    if (q.options.length < 2) error('$ctx needs at least 2 options');
    checkUnique(q.options.map((o) => o.id), '$ctx option');
    if (!q.options.any((o) => o.id == q.correctOptionId)) {
      error('$ctx: correct_option_id "${q.correctOptionId}" is not one of its options');
    }
    if (q.explanation.isEmpty) error('$ctx has no explanation');

    // Every language the question is written in must cover options and explanation too.
    for (final language in q.text.languages) {
      for (final o in q.options) {
        if (!o.text.has(language)) error('$ctx option ${o.id} is missing ${language.name} text');
      }
      if (!q.explanation.has(language)) warn('$ctx has no ${language.name} explanation');
    }
    final fixedLanguage = subjectLanguage[q.subjectId];
    if (fixedLanguage != null) {
      if (!q.text.has(fixedLanguage)) error('$ctx is not written in ${fixedLanguage.name}, the language it tests');
    } else {
      for (final language in AppLanguage.values) {
        if (!q.text.has(language)) warn('$ctx has no ${language.name} translation');
      }
    }
    if (q.verificationStatus != VerificationStatus.verified) {
      (pack.releaseReady ? error : warn)('$ctx is not verified (${q.verificationStatus.code})');
    }
  }

  for (final p in pack.papers) {
    final ctx = 'Paper "${p.id}"';
    if (p.title.isEmpty) error('$ctx has no title');
    if (p.questionIds.isEmpty) error('$ctx has no questions');
    if (p.questionCount != p.questionIds.length) {
      error('$ctx declares question_count ${p.questionCount} but lists ${p.questionIds.length} questions');
    }
    checkUnique(p.questionIds, '$ctx question');
    for (final id in p.questionIds) {
      if (!questionsById.containsKey(id)) error('$ctx lists unknown question "$id"');
    }
    if (!p.distributionCleared) {
      (pack.releaseReady ? error : warn)('$ctx has no recorded permission to distribute it');
    }
    if (p.marking.correct <= 0) error('$ctx: marks for a correct answer must be positive');
    if (p.marking.incorrect > 0) error('$ctx: marks for a wrong answer cannot be positive');
    if (p.isOfficialPyq) {
      if (p.year == null) error('$ctx is marked official but has no year');
      if (p.exam == null || p.level == null) error('$ctx is marked official but has no exam or level');
      final unverified = p.questionIds
          .where((id) => questionsById[id]?.verificationStatus != VerificationStatus.verified);
      if (unverified.isNotEmpty && pack.releaseReady) {
        error('$ctx is marked official but has unverified questions: ${unverified.join(', ')}');
      }
    }
    final pdf = p.pdfAsset;
    if (pdf != null && assetExists != null && !assetExists(pdf)) {
      error('$ctx: PDF "$pdf" does not exist');
    }
  }

  if (!pack.releaseReady) {
    warn('Pack ${pack.contentVersion} is not marked release_ready; '
        'set it once every paper has permission to be distributed');
  }
  return issues;
}
