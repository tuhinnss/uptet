import 'dart:convert';

import 'package:sqflite/sqflite.dart';

import '../models/attempt.dart';
import '../models/content.dart';
import '../models/content_index.dart';
import '../models/revision.dart';
import '../services/progress_calculator.dart';
import '../services/revision_scheduler.dart';
import '../services/scoring.dart';
import '../services/study_activity.dart';

class RevisionOverview {
  const RevisionOverview({
    required this.due,
    required this.upcoming,
    required this.mastered,
    required this.nextDueAt,
  });

  final int due;
  final int upcoming;
  final int mastered;

  /// Earliest future review, when nothing is due now.
  final DateTime? nextDueAt;

  int get active => due + upcoming;
}

class ProgressReport {
  const ProgressReport({
    required this.testsCompleted,
    required this.correct,
    required this.incorrect,
    required this.unanswered,
    required this.revision,
    required this.topics,
    required this.attempts,
    required this.papersCompleted,
    required this.distinctQuestionsAttempted,
    required this.studyDays,
  });

  final int testsCompleted;
  final int correct;
  final int incorrect;
  final int unanswered;
  final RevisionOverview revision;
  final List<TopicPerformance> topics;

  /// Submitted attempts, newest first.
  final List<Attempt> attempts;

  /// Different papers submitted at least once.
  final int papersCompleted;

  /// Different questions answered in submitted attempts.
  final int distinctQuestionsAttempted;

  /// Days with any study activity, oldest first.
  final List<StudyDay> studyDays;

  int get attempted => correct + incorrect;
  double? get accuracyPercent => accuracyPercentOf(correct, attempted);
}

class ReviewOutcome {
  const ReviewOutcome({required this.isCorrect, required this.state});

  final bool isCorrect;
  final RevisionState state;
}

/// Learner records: attempts, answers, revision schedule and review history.
class ProgressRepository {
  ProgressRepository(this._db, {this.scheduler = const RevisionScheduler(), DateTime Function()? clock})
      : _clock = clock ?? DateTime.now;

  final Database _db;
  final RevisionScheduler scheduler;
  final DateTime Function() _clock;

  // ---- Attempts -----------------------------------------------------------

  Future<int> startAttempt({
    required AttemptKind kind,
    String? paperId,
    String? topicId,
    required List<Question> questions,
    required MarkingScheme marking,
    required String contentVersion,
    AttemptMode mode = AttemptMode.practice,
    Duration? timeLimit,
  }) {
    final now = _clock().millisecondsSinceEpoch;
    return _db.transaction((txn) async {
      final id = await txn.insert('attempts', {
        'kind': kind.name,
        'mode': mode.name,
        'time_limit_seconds': timeLimit?.inSeconds,
        'paper_id': paperId,
        'topic_id': topicId,
        'question_ids_json': jsonEncode([for (final q in questions) q.id]),
        'marking_scheme_json': jsonEncode(marking.toJson()),
        'content_version': contentVersion,
        'status': AttemptStatus.inProgress.code,
        'current_index': 0,
        'started_at': now,
        'updated_at': now,
        'total_questions': questions.length,
      });
      final batch = txn.batch();
      for (final q in questions) {
        batch.insert('user_answers', {'attempt_id': id, 'question_id': q.id});
      }
      await batch.commit(noResult: true);
      return id;
    });
  }

  /// Saves the learner's choice for one question of an unfinished attempt.
  Future<void> saveAnswer(int attemptId, String questionId, String? optionId) async {
    final now = _clock().millisecondsSinceEpoch;
    await _db.transaction((txn) async {
      await _requireInProgress(txn, attemptId);
      final previous = await txn.query('user_answers',
          columns: ['selected_option_id'], where: 'attempt_id = ? AND question_id = ?', whereArgs: [attemptId, questionId]);
      final updated = await txn.update(
        'user_answers',
        {'selected_option_id': optionId, 'answered_at': optionId == null ? null : now},
        where: 'attempt_id = ? AND question_id = ?',
        whereArgs: [attemptId, questionId],
      );
      if (updated != 1) throw StateError('Question $questionId is not part of attempt $attemptId');
      // Changing an answer is not another question studied.
      if (optionId != null && previous.single['selected_option_id'] == null) {
        await _addStudy(txn, questions: 1);
      }
      await txn.update('attempts', {'updated_at': now}, where: 'attempt_id = ?', whereArgs: [attemptId]);
    });
  }

  Future<void> saveCurrentIndex(int attemptId, int index) => _db.update(
        'attempts',
        {'current_index': index, 'updated_at': _clock().millisecondsSinceEpoch},
        where: 'attempt_id = ? AND status = ?',
        whereArgs: [attemptId, AttemptStatus.inProgress.code],
      );

  /// Records the time spent so far; only an unfinished attempt's clock moves.
  /// The time added since the last save counts as today's study time.
  Future<void> saveElapsed(int attemptId, Duration elapsed) => _db.transaction((txn) async {
        final rows = await txn.query('attempts',
            columns: ['elapsed_seconds'],
            where: 'attempt_id = ? AND status = ?',
            whereArgs: [attemptId, AttemptStatus.inProgress.code]);
        if (rows.isEmpty) return;
        await txn.update('attempts', {'elapsed_seconds': elapsed.inSeconds},
            where: 'attempt_id = ?', whereArgs: [attemptId]);
        final added = elapsed.inSeconds - (rows.single['elapsed_seconds'] as int);
        if (added > 0) await _addStudy(txn, seconds: added);
      });

  /// Deletes an unfinished attempt. Submitted attempts are never deleted.
  Future<void> discardInProgress(int attemptId) => _db.delete(
        'attempts',
        where: 'attempt_id = ? AND status = ?',
        whereArgs: [attemptId, AttemptStatus.inProgress.code],
      );

  /// Scores and saves the attempt, then schedules revision for wrong answers,
  /// all in one transaction. Submitting twice keeps the first result.
  Future<Attempt> submitAttempt(int attemptId, ContentIndex content) async {
    final now = _clock();
    await _db.transaction((txn) async {
      final attempt = await _loadAttempt(txn, attemptId);
      if (attempt == null) throw StateError('Attempt $attemptId not found');
      if (attempt.isSubmitted) return;

      final questions = [
        for (final id in attempt.questionIds)
          content.question(id) ?? (throw StateError('Question $id is missing from installed content')),
      ];
      final result = scoreAnswers(
        questions: questions,
        selected: {for (final a in attempt.answers.values) a.questionId: a.selectedOptionId},
        marking: attempt.marking,
      );

      for (final a in result.answers) {
        await txn.update(
          'user_answers',
          {'correct_option_id': a.correctOptionId, 'is_correct': a.isCorrect ? 1 : 0},
          where: 'attempt_id = ? AND question_id = ?',
          whereArgs: [attemptId, a.questionId],
        );
        if (a.isAnswered && !a.isCorrect) {
          await _scheduleFromTest(txn, a.questionId, attemptId, now);
        }
      }

      await txn.update(
        'attempts',
        {
          'status': AttemptStatus.submitted.code,
          'submitted_at': now.millisecondsSinceEpoch,
          'updated_at': now.millisecondsSinceEpoch,
          'score': result.score,
          'max_score': result.maxScore,
          'correct_count': result.correct,
          'incorrect_count': result.incorrect,
          'unanswered_count': result.unanswered,
        },
        where: 'attempt_id = ?',
        whereArgs: [attemptId],
      );
    });
    return (await loadAttempt(attemptId))!;
  }

  Future<Attempt?> loadAttempt(int attemptId) => _loadAttempt(_db, attemptId);

  Future<Attempt?> latestInProgress() async {
    final rows = await _db.query('attempts',
        where: 'status = ?', whereArgs: [AttemptStatus.inProgress.code], orderBy: 'updated_at DESC', limit: 1);
    return rows.isEmpty ? null : _loadAttempt(_db, rows.first['attempt_id'] as int);
  }

  Future<Attempt?> inProgressFor({String? paperId, String? topicId}) async {
    final rows = await _db.query(
      'attempts',
      where: 'status = ? AND ${paperId != null ? 'paper_id' : 'topic_id'} = ?',
      whereArgs: [AttemptStatus.inProgress.code, paperId ?? topicId],
      orderBy: 'updated_at DESC',
      limit: 1,
    );
    return rows.isEmpty ? null : _loadAttempt(_db, rows.first['attempt_id'] as int);
  }

  /// Submitted attempts, newest first, optionally for one paper.
  Future<List<Attempt>> submittedAttempts({String? paperId}) async {
    final rows = await _db.query(
      'attempts',
      where: 'status = ?${paperId != null ? ' AND paper_id = ?' : ''}',
      whereArgs: [AttemptStatus.submitted.code, if (paperId != null) paperId],
      orderBy: 'submitted_at DESC',
    );
    return [for (final r in rows) _attemptFromRow(r, const {})];
  }

  Future<void> _requireInProgress(DatabaseExecutor db, int attemptId) async {
    final rows = await db.query('attempts', columns: ['status'], where: 'attempt_id = ?', whereArgs: [attemptId]);
    if (rows.isEmpty || rows.first['status'] != AttemptStatus.inProgress.code) {
      throw StateError('Attempt $attemptId is not in progress');
    }
  }

  Future<Attempt?> _loadAttempt(DatabaseExecutor db, int attemptId) async {
    final rows = await db.query('attempts', where: 'attempt_id = ?', whereArgs: [attemptId]);
    if (rows.isEmpty) return null;
    final answerRows = await db.query('user_answers', where: 'attempt_id = ?', whereArgs: [attemptId]);
    final answers = {
      for (final r in answerRows)
        r['question_id'] as String: AnswerRecord(
          questionId: r['question_id'] as String,
          selectedOptionId: r['selected_option_id'] as String?,
          correctOptionId: r['correct_option_id'] as String?,
          isCorrect: r['is_correct'] == null ? null : r['is_correct'] == 1,
        ),
    };
    return _attemptFromRow(rows.first, answers);
  }

  Attempt _attemptFromRow(Map<String, Object?> r, Map<String, AnswerRecord> answers) {
    DateTime? time(String key) =>
        r[key] == null ? null : DateTime.fromMillisecondsSinceEpoch(r[key] as int);
    return Attempt(
      id: r['attempt_id'] as int,
      kind: AttemptKind.values.byName(r['kind'] as String),
      mode: AttemptMode.fromCode(r['mode'] as String?),
      timeLimit: r['time_limit_seconds'] == null ? null : Duration(seconds: r['time_limit_seconds'] as int),
      elapsed: Duration(seconds: r['elapsed_seconds'] as int? ?? 0),
      paperId: r['paper_id'] as String?,
      topicId: r['topic_id'] as String?,
      questionIds: (jsonDecode(r['question_ids_json'] as String) as List).cast<String>(),
      marking: MarkingScheme.fromJson(jsonDecode(r['marking_scheme_json'] as String), 'marking'),
      contentVersion: r['content_version'] as String,
      status: AttemptStatus.fromCode(r['status'] as String),
      currentIndex: r['current_index'] as int,
      startedAt: time('started_at')!,
      updatedAt: time('updated_at')!,
      submittedAt: time('submitted_at'),
      score: (r['score'] as num?)?.toDouble(),
      maxScore: (r['max_score'] as num?)?.toDouble(),
      correctCount: r['correct_count'] as int?,
      incorrectCount: r['incorrect_count'] as int?,
      unansweredCount: r['unanswered_count'] as int?,
      answers: answers,
    );
  }

  // ---- Revision -----------------------------------------------------------

  /// One revision row per question: a wrong test answer creates it, or puts an
  /// existing (even mastered) question back at the start of the sequence.
  Future<void> _scheduleFromTest(Transaction txn, String questionId, int attemptId, DateTime now) async {
    final rows = await txn.query('revision_items', where: 'question_id = ?', whereArgs: [questionId]);
    final current = rows.isEmpty ? null : _revisionFromRow(rows.first).state;
    final state = scheduler.afterIncorrectInTest(now, current: current);
    final values = {..._stateColumns(state), 'source_attempt_id': attemptId};
    if (rows.isEmpty) {
      await txn.insert('revision_items', {
        ...values,
        'question_id': questionId,
        'created_at': now.millisecondsSinceEpoch,
      });
    } else {
      await txn.update('revision_items', values, where: 'question_id = ?', whereArgs: [questionId]);
    }
  }

  /// Active items, due ones first.
  Future<List<RevisionItem>> activeRevisionItems() async {
    final rows = await _db.query('revision_items',
        where: 'status = ?', whereArgs: [RevisionStatus.active.name], orderBy: 'next_review_at, revision_id');
    return [for (final r in rows) _revisionFromRow(r)];
  }

  Future<List<RevisionItem>> dueRevisionItems() async {
    final now = _clock();
    return [for (final item in await activeRevisionItems()) if (item.state.isDue(now)) item];
  }

  Future<List<RevisionItem>> masteredRevisionItems() async {
    final rows = await _db.query('revision_items',
        where: 'status = ?', whereArgs: [RevisionStatus.mastered.name], orderBy: 'last_reviewed_at DESC');
    return [for (final r in rows) _revisionFromRow(r)];
  }

  Future<RevisionOverview> revisionOverview() async {
    final now = _clock();
    final active = await activeRevisionItems();
    final due = active.where((i) => i.state.isDue(now)).length;
    final upcoming = active.where((i) => !i.state.isDue(now)).toList();
    final mastered = Sqflite.firstIntValue(await _db.rawQuery(
            'SELECT COUNT(*) FROM revision_items WHERE status = ?', [RevisionStatus.mastered.name])) ??
        0;
    return RevisionOverview(
      due: due,
      upcoming: upcoming.length,
      mastered: mastered,
      nextDueAt: upcoming.isEmpty ? null : upcoming.first.state.nextReviewAt,
    );
  }

  /// Records a review answer and moves the question along its schedule.
  Future<ReviewOutcome> recordReview(int revisionId, String selectedOptionId, ContentIndex content) {
    final now = _clock();
    return _db.transaction((txn) async {
      final rows = await txn.query('revision_items', where: 'revision_id = ?', whereArgs: [revisionId]);
      if (rows.isEmpty) throw StateError('Revision item $revisionId not found');
      final item = _revisionFromRow(rows.first);
      final question = content.question(item.questionId) ??
          (throw StateError('Question ${item.questionId} is missing from installed content'));
      final isCorrect = selectedOptionId == question.correctOptionId;
      final next = scheduler.afterReview(item.state, correct: isCorrect, now: now);
      await txn.update('revision_items', _stateColumns(next), where: 'revision_id = ?', whereArgs: [revisionId]);
      await txn.insert('review_log', {
        'revision_id': revisionId,
        'question_id': item.questionId,
        'selected_option_id': selectedOptionId,
        'is_correct': isCorrect ? 1 : 0,
        'reviewed_at': now.millisecondsSinceEpoch,
        'stage_before': item.state.stage,
        'stage_after': next.stage,
      });
      await _addStudy(txn, questions: 1);
      return ReviewOutcome(isCorrect: isCorrect, state: next);
    });
  }

  Map<String, Object?> _stateColumns(RevisionState s) => {
        'review_stage': s.stage,
        'status': s.status.name,
        'next_review_at': s.nextReviewAt.millisecondsSinceEpoch,
        'last_reviewed_at': s.lastReviewedAt?.millisecondsSinceEpoch,
        'consecutive_correct_reviews': s.consecutiveCorrect,
      };

  RevisionItem _revisionFromRow(Map<String, Object?> r) => RevisionItem(
        id: r['revision_id'] as int,
        questionId: r['question_id'] as String,
        sourceAttemptId: r['source_attempt_id'] as int?,
        createdAt: DateTime.fromMillisecondsSinceEpoch(r['created_at'] as int),
        state: RevisionState(
          stage: r['review_stage'] as int,
          status: RevisionStatus.fromCode(r['status'] as String),
          nextReviewAt: DateTime.fromMillisecondsSinceEpoch(r['next_review_at'] as int),
          lastReviewedAt: r['last_reviewed_at'] == null
              ? null
              : DateTime.fromMillisecondsSinceEpoch(r['last_reviewed_at'] as int),
          consecutiveCorrect: r['consecutive_correct_reviews'] as int,
        ),
      );

  // ---- Study activity -----------------------------------------------------

  /// Adds to today's totals. No UPSERT: older Android SQLite lacks it.
  Future<void> _addStudy(DatabaseExecutor db, {int questions = 0, int seconds = 0}) async {
    final day = dayKey(_clock());
    final updated = await db.rawUpdate(
        'UPDATE study_days SET questions = questions + ?, seconds = seconds + ? WHERE day = ?', [questions, seconds, day]);
    if (updated == 0) await db.insert('study_days', {'day': day, 'questions': questions, 'seconds': seconds});
  }

  /// Every recorded day, oldest first.
  Future<List<StudyDay>> studyDays() async {
    final rows = await _db.query('study_days', orderBy: 'day');
    return [
      for (final r in rows)
        StudyDay(day: parseDayKey(r['day'] as String), questions: r['questions'] as int, seconds: r['seconds'] as int),
    ];
  }

  // ---- Progress -----------------------------------------------------------

  Future<ProgressReport> progressReport() async {
    final totals = (await _db.rawQuery('''
      SELECT COUNT(*) AS tests,
             COALESCE(SUM(correct_count), 0) AS correct,
             COALESCE(SUM(incorrect_count), 0) AS incorrect,
             COALESCE(SUM(unanswered_count), 0) AS unanswered
      FROM attempts WHERE status = ?''', [AttemptStatus.submitted.code])).first;
    final topicRows = await _db.rawQuery('''
      SELECT q.topic_id, ua.is_correct
      FROM user_answers ua
      JOIN attempts a ON a.attempt_id = ua.attempt_id
      JOIN questions q ON q.question_id = ua.question_id
      WHERE a.status = ? AND ua.selected_option_id IS NOT NULL''', [AttemptStatus.submitted.code]);
    final distinct = (await _db.rawQuery('''
      SELECT (SELECT COUNT(DISTINCT paper_id) FROM attempts WHERE status = ? AND kind = 'paper') AS papers,
             (SELECT COUNT(DISTINCT ua.question_id) FROM user_answers ua
                JOIN attempts a ON a.attempt_id = ua.attempt_id
                WHERE a.status = ? AND ua.selected_option_id IS NOT NULL) AS questions''',
        [AttemptStatus.submitted.code, AttemptStatus.submitted.code])).first;
    return ProgressReport(
      testsCompleted: totals['tests'] as int,
      correct: totals['correct'] as int,
      incorrect: totals['incorrect'] as int,
      unanswered: totals['unanswered'] as int,
      revision: await revisionOverview(),
      topics: topicPerformance([
        for (final r in topicRows) (topicId: r['topic_id'] as String, isCorrect: r['is_correct'] == 1),
      ]),
      attempts: await submittedAttempts(),
      papersCompleted: distinct['papers'] as int,
      distinctQuestionsAttempted: distinct['questions'] as int,
      studyDays: await studyDays(),
    );
  }
}
