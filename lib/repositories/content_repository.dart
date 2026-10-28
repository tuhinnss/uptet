import 'dart:convert';

import 'package:sqflite/sqflite.dart';

import '../models/content.dart';
import '../models/content_index.dart';

/// Installs bundled content packs into SQLite and reads them back.
class ContentRepository {
  ContentRepository(this._db);

  final Database _db;

  Future<String?> installedVersion() async {
    final rows = await _db.query('content_meta',
        columns: ['value'], where: 'key = ?', whereArgs: ['content_version']);
    return rows.isEmpty ? null : rows.first['value'] as String;
  }

  /// Installs [pack] in one transaction, so a failure leaves the previous
  /// content untouched. Rows missing from the pack are retired, never deleted,
  /// so past attempts keep pointing at their questions.
  Future<void> importPack(ContentPack pack) async {
    await _db.transaction((txn) async {
      for (final table in const ['subjects', 'topics', 'papers', 'questions']) {
        await txn.update(table, {'is_active': 0});
      }
      for (final s in pack.subjects) {
        await _upsert(txn, 'subjects', 'subject_id', {
          'subject_id': s.id,
          'name_en': s.name.en,
          'name_hi': s.name.hi,
          'language': s.language?.name,
          'sort_order': s.sortOrder,
          'is_active': 1,
        });
      }
      for (final t in pack.topics) {
        await _upsert(txn, 'topics', 'topic_id', {
          'topic_id': t.id,
          'subject_id': t.subjectId,
          'name_en': t.name.en,
          'name_hi': t.name.hi,
          'sort_order': t.sortOrder,
          'is_active': 1,
        });
      }
      final questionsById = {for (final q in pack.questions) q.id: q};
      final subjectLanguage = {for (final s in pack.subjects) s.id: s.language};
      for (final p in pack.papers) {
        final languages = paperLanguagesOf([
          for (final id in p.questionIds)
            if (questionsById[id] case final q?) q,
        ], (subjectId) => subjectLanguage[subjectId]);
        await _upsert(txn, 'papers', 'paper_id', {
          'paper_id': p.id,
          'title_en': p.title.en,
          'title_hi': p.title.hi,
          'year': p.year,
          'paper_code': p.paperCode,
          'exam': p.exam?.name,
          'level': p.level?.name,
          'question_ids_json': jsonEncode(p.questionIds),
          'is_official_pyq': p.isOfficialPyq ? 1 : 0,
          'distribution_cleared': p.distributionCleared ? 1 : 0,
          'language_availability': languages.map((l) => l.name).join(','),
          'duration_minutes': p.durationMinutes,
          'marking_scheme_json': jsonEncode(p.marking.toJson()),
          'pdf_asset_path': p.pdfAsset,
          'question_count': p.questionIds.length,
          'source_reference': p.source,
          'sort_order': p.sortOrder,
          'content_version': pack.contentVersion,
          'is_active': 1,
        });
      }
      for (final q in pack.questions) {
        await _upsert(txn, 'questions', 'question_id', {
          'question_id': q.id,
          'paper_id': null,
          'paper_position': null,
          'subject_id': q.subjectId,
          'topic_id': q.topicId,
          'question_text_hi': q.text.hi,
          'question_text_en': q.text.en,
          'options_json': jsonEncode([
            for (final o in q.options) {'id': o.id, 'en': o.text.en, 'hi': o.text.hi},
          ]),
          'correct_option_id': q.correctOptionId,
          'explanation_hi': q.explanation.hi,
          'explanation_en': q.explanation.en,
          'source_reference': q.source,
          'verification_status': q.verificationStatus.code,
          'sort_order': q.sortOrder,
          'content_version': pack.contentVersion,
          'is_active': 1,
        });
      }
      await _upsert(txn, 'content_meta', 'key', {'key': 'content_version', 'value': pack.contentVersion});
      await _upsert(txn, 'content_meta', 'key', {'key': 'release_ready', 'value': pack.releaseReady ? '1' : '0'});
    });
  }

  Future<void> _upsert(Transaction txn, String table, String keyColumn, Map<String, Object?> row) async {
    final updated = await txn.update(table, row, where: '$keyColumn = ?', whereArgs: [row[keyColumn]]);
    if (updated == 0) await txn.insert(table, row);
  }

  Future<ContentIndex> loadIndex() async {
    final meta = {
      for (final row in await _db.query('content_meta')) row['key'] as String: row['value'] as String,
    };
    final subjectRows = await _db.query('subjects');
    final topicRows = await _db.query('topics');
    final paperRows = await _db.query('papers');
    final questionRows = await _db.query('questions', orderBy: 'sort_order');

    Set<String> activeIds(List<Map<String, Object?>> rows, String key) =>
        {for (final r in rows) if (r['is_active'] == 1) r[key] as String};

    // Papers installed before schema v3 have no question list of their own.
    final legacyPaperQuestions = <String, List<(int, String)>>{};
    for (final r in questionRows) {
      final paperId = r['paper_id'] as String?;
      if (paperId != null && r['is_active'] == 1) {
        (legacyPaperQuestions[paperId] ??= []).add((r['paper_position'] as int, r['question_id'] as String));
      }
    }
    List<String> paperQuestionIds(Map<String, Object?> r) {
      final json = r['question_ids_json'] as String?;
      if (json != null) return (jsonDecode(json) as List).cast<String>();
      final legacy = legacyPaperQuestions[r['paper_id']] ?? <(int, String)>[];
      return [for (final (_, id) in legacy..sort((a, b) => a.$1.compareTo(b.$1))) id];
    }

    return ContentIndex(
      contentVersion: meta['content_version'] ?? '',
      releaseReady: meta['release_ready'] == '1',
      subjects: [
        for (final r in subjectRows)
          Subject(
            id: r['subject_id'] as String,
            name: LocalizedText(en: r['name_en'] as String?, hi: r['name_hi'] as String?),
            sortOrder: r['sort_order'] as int,
            language: AppLanguage.fromCode(r['language'] as String?),
          ),
      ],
      topics: [
        for (final r in topicRows)
          Topic(
            id: r['topic_id'] as String,
            subjectId: r['subject_id'] as String,
            name: LocalizedText(en: r['name_en'] as String?, hi: r['name_hi'] as String?),
            sortOrder: r['sort_order'] as int,
          ),
      ],
      papers: [
        for (final r in paperRows)
          Paper(
            id: r['paper_id'] as String,
            title: LocalizedText(en: r['title_en'] as String?, hi: r['title_hi'] as String?),
            year: r['year'] as int?,
            paperCode: r['paper_code'] as String?,
            exam: _enumByName(Exam.values, r['exam']),
            level: _enumByName(ExamLevel.values, r['level']),
            isOfficialPyq: r['is_official_pyq'] == 1,
            distributionCleared: r['distribution_cleared'] == 1,
            durationMinutes: r['duration_minutes'] as int?,
            marking: MarkingScheme.fromJson(jsonDecode(r['marking_scheme_json'] as String), 'marking'),
            pdfAsset: r['pdf_asset_path'] as String?,
            source: r['source_reference'] as String,
            questionIds: paperQuestionIds(r),
            questionCount: r['question_count'] as int,
            sortOrder: r['sort_order'] as int,
          ),
      ],
      questions: [for (final r in questionRows) _questionFromRow(r)],
      activeSubjectIds: activeIds(subjectRows, 'subject_id'),
      activeTopicIds: activeIds(topicRows, 'topic_id'),
      activePaperIds: activeIds(paperRows, 'paper_id'),
      activeQuestionIds: activeIds(questionRows, 'question_id'),
    );
  }

  Question _questionFromRow(Map<String, Object?> r) {
    final options = (jsonDecode(r['options_json'] as String) as List).cast<Map<String, Object?>>();
    return Question(
      id: r['question_id'] as String,
      subjectId: r['subject_id'] as String,
      topicId: r['topic_id'] as String,
      text: LocalizedText(en: r['question_text_en'] as String?, hi: r['question_text_hi'] as String?),
      options: [
        for (final o in options)
          AnswerOption(
            id: o['id'] as String,
            text: LocalizedText(en: o['en'] as String?, hi: o['hi'] as String?),
          ),
      ],
      correctOptionId: r['correct_option_id'] as String,
      explanation: LocalizedText(en: r['explanation_en'] as String?, hi: r['explanation_hi'] as String?),
      source: r['source_reference'] as String,
      verificationStatus:
          VerificationStatus.fromCode(r['verification_status'] as String) ?? VerificationStatus.draft,
      sortOrder: r['sort_order'] as int,
    );
  }
}

/// A stored enum value; unknown codes (from a newer app version) read as null.
T? _enumByName<T extends Enum>(List<T> values, Object? name) {
  for (final value in values) {
    if (value.name == name) return value;
  }
  return null;
}
