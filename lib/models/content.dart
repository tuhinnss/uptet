// Content models shared by the app and `tool/validate_content.dart`.
// Keep this file free of Flutter imports so the validator runs with `dart run`.

enum AppLanguage {
  en,
  hi;

  AppLanguage get other => this == en ? hi : en;

  static AppLanguage? fromCode(String? code) {
    for (final language in values) {
      if (language.name == code) return language;
    }
    return null;
  }
}

/// One piece of text in Hindi and/or English. Translations of the same
/// question live together so they always share one stable ID.
class LocalizedText {
  const LocalizedText({this.en, this.hi});

  final String? en;
  final String? hi;

  factory LocalizedText.fromJson(Object? json, String field) {
    if (json is! Map) {
      throw FormatException('$field must be an object with "en" and/or "hi"');
    }
    String? read(String key) {
      final value = json[key];
      if (value == null) return null;
      if (value is! String) throw FormatException('$field.$key must be a string');
      final trimmed = value.trim();
      return trimmed.isEmpty ? null : trimmed;
    }

    return LocalizedText(en: read('en'), hi: read('hi'));
  }

  String? operator [](AppLanguage language) =>
      language == AppLanguage.hi ? hi : en;

  bool has(AppLanguage language) => this[language] != null;

  bool get isEmpty => en == null && hi == null;

  Set<AppLanguage> get languages => {
        for (final language in AppLanguage.values)
          if (has(language)) language,
      };

  /// Text in [language], falling back to the other language. Callers must
  /// tell the learner when [ResolvedText.isFallback] is true.
  ResolvedText resolve(AppLanguage language) {
    final own = this[language];
    if (own != null) return ResolvedText(own, language, isFallback: false);
    return ResolvedText(this[language.other] ?? '', language.other,
        isFallback: true);
  }
}

class ResolvedText {
  const ResolvedText(this.text, this.language, {required this.isFallback});

  final String text;
  final AppLanguage language;
  final bool isFallback;
}

enum VerificationStatus {
  draft('draft'),
  pendingReview('pending_review'),
  verified('verified');

  const VerificationStatus(this.code);

  final String code;

  static VerificationStatus? fromCode(String? code) {
    for (final status in values) {
      if (status.code == code) return status;
    }
    return null;
  }
}

/// Marks per question outcome. Negative marking is a negative [incorrect].
class MarkingScheme {
  const MarkingScheme({required this.correct, this.incorrect = 0, this.unanswered = 0});

  static const oneMarkNoNegative = MarkingScheme(correct: 1);

  final double correct;
  final double incorrect;
  final double unanswered;

  factory MarkingScheme.fromJson(Object? json, String field) {
    if (json is! Map) throw FormatException('$field must be an object');
    double read(String key, {required bool required}) {
      final value = json[key];
      if (value == null && !required) return 0;
      if (value is! num) throw FormatException('$field.$key must be a number');
      return value.toDouble();
    }

    return MarkingScheme(
      correct: read('correct', required: true),
      incorrect: read('incorrect', required: false),
      unanswered: read('unanswered', required: false),
    );
  }

  Map<String, double> toJson() =>
      {'correct': correct, 'incorrect': incorrect, 'unanswered': unanswered};
}

class Subject {
  const Subject({required this.id, required this.name, required this.sortOrder, this.language});

  final String id;
  final LocalizedText name;
  final int sortOrder;

  /// Set for a language subject (Hindi, English) whose questions test that
  /// language, so they are written only in it and are never translated.
  final AppLanguage? language;
}

/// The exam a previous-year paper was set for, in the order the header offers them.
enum Exam {
  uptet,
  supertet,
  ctet;

  static Exam? fromCode(String? code) {
    for (final exam in values) {
      if (exam.name == code) return exam;
    }
    return null;
  }
}

/// Teaching level of a paper: classes I–V or VI–VIII.
enum ExamLevel { primary, junior }

class Topic {
  const Topic({
    required this.id,
    required this.subjectId,
    required this.name,
    required this.sortOrder,
  });

  final String id;
  final String subjectId;
  final LocalizedText name;
  final int sortOrder;
}

class Paper {
  const Paper({
    required this.id,
    required this.title,
    required this.year,
    required this.paperCode,
    required this.isOfficialPyq,
    required this.distributionCleared,
    required this.durationMinutes,
    required this.marking,
    required this.pdfAsset,
    required this.source,
    required this.questionIds,
    required this.questionCount,
    required this.sortOrder,
    this.exam,
    this.level,
  });

  final String id;
  final LocalizedText title;
  final int? year;
  final String? paperCode;

  /// Exam and level the paper belongs to; required for official papers and
  /// used to group them. Practice sets leave both empty.
  final Exam? exam;
  final ExamLevel? level;

  /// Only true once the paper's provenance has been checked. Unchecked sets
  /// must never be presented as official previous-year papers.
  final bool isOfficialPyq;

  /// Set once the rights holder has allowed the paper to be distributed in the
  /// app (always true for original content). Release-ready packs require it.
  final bool distributionCleared;
  final int? durationMinutes;
  final MarkingScheme marking;

  /// Bundled PDF, only for material cleared for redistribution.
  final String? pdfAsset;
  final String source;

  /// Question IDs in exam order. Papers that share sections (the UPTET junior
  /// papers share parts I–III) list the same questions.
  final List<String> questionIds;

  /// Count declared by the content maintainer, checked against [questionIds].
  final int questionCount;
  final int sortOrder;
}

class AnswerOption {
  const AnswerOption({required this.id, required this.text});

  final String id;
  final LocalizedText text;
}

class Question {
  const Question({
    required this.id,
    required this.subjectId,
    required this.topicId,
    required this.text,
    required this.options,
    required this.correctOptionId,
    required this.explanation,
    required this.source,
    required this.verificationStatus,
    required this.sortOrder,
  });

  final String id;
  final String subjectId;
  final String topicId;
  final LocalizedText text;
  final List<AnswerOption> options;
  final String correctOptionId;
  final LocalizedText explanation;
  final String source;
  final VerificationStatus verificationStatus;
  final int sortOrder;

  /// Languages in which the question, every option and the explanation exist.
  Set<AppLanguage> get languages => {
        for (final language in AppLanguage.values)
          if (text.has(language) &&
              explanation.has(language) &&
              options.every((o) => o.text.has(language)))
            language,
      };

  /// [preferred] when fully translated, otherwise the language that is.
  AppLanguage displayLanguage(AppLanguage preferred) {
    final available = languages;
    if (available.contains(preferred) || available.isEmpty) return preferred;
    return available.first;
  }
}

/// Languages a paper can be taken in: those every question is fully written
/// in. Questions of a language subject are left out, since they exist only in
/// the language they test.
Set<AppLanguage> paperLanguagesOf(
    List<Question> questions, AppLanguage? Function(String subjectId) subjectLanguage) {
  Set<AppLanguage>? common;
  for (final q in questions) {
    if (subjectLanguage(q.subjectId) != null) continue;
    common = common == null ? {...q.languages} : common.intersection(q.languages);
  }
  return common ?? {for (final q in questions) ...q.languages};
}

/// The bundled content file (`assets/content/content_pack.json`).
class ContentPack {
  const ContentPack({
    required this.schemaVersion,
    required this.contentVersion,
    required this.releaseReady,
    required this.subjects,
    required this.topics,
    required this.papers,
    required this.questions,
  });

  static const supportedSchemaVersion = 1;

  final int schemaVersion;
  final String contentVersion;

  /// Set by the content maintainer only when every question is verified.
  final bool releaseReady;
  final List<Subject> subjects;
  final List<Topic> topics;
  final List<Paper> papers;
  final List<Question> questions;

  /// Parses the pack, throwing [FormatException] for structural problems.
  /// Cross-references are checked separately by `validateContentPack`.
  factory ContentPack.fromJson(Object? json) {
    final root = _map(json, 'content pack');
    final schemaVersion = _int(root, 'schema_version', 'content pack');
    if (schemaVersion != supportedSchemaVersion) {
      throw FormatException(
          'Unsupported schema_version $schemaVersion (expected $supportedSchemaVersion)');
    }

    final subjects = <Subject>[];
    final topics = <Topic>[];
    final subjectList = _list(root, 'subjects', 'content pack');
    for (var i = 0; i < subjectList.length; i++) {
      final s = _map(subjectList[i], 'subjects[$i]');
      final subjectId = _string(s, 'id', 'subjects[$i]');
      subjects.add(Subject(
        id: subjectId,
        name: LocalizedText.fromJson(s['name'], 'subject $subjectId name'),
        sortOrder: i,
        language: _optEnum(s, 'language', 'subject $subjectId', AppLanguage.values),
      ));
      final topicList = _list(s, 'topics', 'subject $subjectId');
      for (var j = 0; j < topicList.length; j++) {
        final t = _map(topicList[j], 'subject $subjectId topics[$j]');
        final topicId = _string(t, 'id', 'subject $subjectId topics[$j]');
        topics.add(Topic(
          id: topicId,
          subjectId: subjectId,
          name: LocalizedText.fromJson(t['name'], 'topic $topicId name'),
          sortOrder: j,
        ));
      }
    }

    final papers = <Paper>[];
    final paperList = _list(root, 'papers', 'content pack');
    for (var i = 0; i < paperList.length; i++) {
      final p = _map(paperList[i], 'papers[$i]');
      final id = _string(p, 'id', 'papers[$i]');
      final ctx = 'paper $id';
      papers.add(Paper(
        id: id,
        title: LocalizedText.fromJson(p['title'], '$ctx title'),
        year: _optInt(p, 'year', ctx),
        paperCode: _optString(p, 'paper_code', ctx),
        exam: _optEnum(p, 'exam', ctx, Exam.values),
        level: _optEnum(p, 'level', ctx, ExamLevel.values),
        isOfficialPyq: _bool(p, 'is_official_pyq', ctx),
        distributionCleared: _bool(p, 'distribution_cleared', ctx),
        durationMinutes: _optInt(p, 'duration_minutes', ctx),
        marking: MarkingScheme.fromJson(p['marking'], '$ctx marking'),
        pdfAsset: _optString(p, 'pdf_asset', ctx),
        source: _string(p, 'source', ctx),
        questionIds: [
          for (final (k, v) in _list(p, 'question_ids', ctx).indexed)
            v is String ? v : throw FormatException('$ctx question_ids[$k] must be a string'),
        ],
        questionCount: _int(p, 'question_count', ctx),
        sortOrder: i,
      ));
    }

    final questions = <Question>[];
    final questionList = _list(root, 'questions', 'content pack');
    for (var i = 0; i < questionList.length; i++) {
      final q = _map(questionList[i], 'questions[$i]');
      final id = _string(q, 'id', 'questions[$i]');
      final ctx = 'question $id';
      final statusCode = _string(q, 'verification_status', ctx);
      final status = VerificationStatus.fromCode(statusCode) ??
          (throw FormatException('$ctx has unknown verification_status "$statusCode"'));
      final options = <AnswerOption>[];
      final optionList = _list(q, 'options', ctx);
      for (var j = 0; j < optionList.length; j++) {
        final o = _map(optionList[j], '$ctx options[$j]');
        final optionId = _string(o, 'id', '$ctx options[$j]');
        options.add(AnswerOption(
          id: optionId,
          text: LocalizedText.fromJson(o['text'], '$ctx option $optionId'),
        ));
      }
      questions.add(Question(
        id: id,
        subjectId: _string(q, 'subject_id', ctx),
        topicId: _string(q, 'topic_id', ctx),
        text: LocalizedText.fromJson(q['text'], '$ctx text'),
        options: options,
        correctOptionId: _string(q, 'correct_option_id', ctx),
        explanation: LocalizedText.fromJson(q['explanation'], '$ctx explanation'),
        source: _string(q, 'source', ctx),
        verificationStatus: status,
        sortOrder: i,
      ));
    }

    return ContentPack(
      schemaVersion: schemaVersion,
      contentVersion: _string(root, 'content_version', 'content pack'),
      releaseReady: _bool(root, 'release_ready', 'content pack'),
      subjects: subjects,
      topics: topics,
      papers: papers,
      questions: questions,
    );
  }
}

Map<String, Object?> _map(Object? value, String ctx) {
  if (value is Map<String, Object?>) return value;
  if (value is Map) return value.cast<String, Object?>();
  throw FormatException('$ctx must be an object');
}

List<Object?> _list(Map<String, Object?> map, String key, String ctx) {
  final value = map[key];
  if (value is List) return value;
  throw FormatException('$ctx: "$key" must be a list');
}

String _string(Map<String, Object?> map, String key, String ctx) {
  final value = map[key];
  if (value is String && value.trim().isNotEmpty) return value.trim();
  throw FormatException('$ctx: "$key" must be a non-empty string');
}

String? _optString(Map<String, Object?> map, String key, String ctx) {
  final value = map[key];
  if (value == null) return null;
  if (value is String) return value.trim().isEmpty ? null : value.trim();
  throw FormatException('$ctx: "$key" must be a string or null');
}

T? _optEnum<T extends Enum>(Map<String, Object?> map, String key, String ctx, List<T> values) {
  final code = _optString(map, key, ctx);
  if (code == null) return null;
  for (final value in values) {
    if (value.name == code) return value;
  }
  throw FormatException('$ctx: unknown $key "$code" (expected ${values.map((v) => v.name).join(', ')})');
}

int _int(Map<String, Object?> map, String key, String ctx) {
  final value = map[key];
  if (value is int) return value;
  throw FormatException('$ctx: "$key" must be a whole number');
}

int? _optInt(Map<String, Object?> map, String key, String ctx) {
  final value = map[key];
  if (value == null || value is int) return value as int?;
  throw FormatException('$ctx: "$key" must be a whole number or null');
}

bool _bool(Map<String, Object?> map, String key, String ctx) {
  final value = map[key];
  if (value is bool) return value;
  throw FormatException('$ctx: "$key" must be true or false');
}
