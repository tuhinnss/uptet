import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';
import 'package:uptet_saathi/database/app_database.dart';
import 'package:uptet_saathi/models/attempt.dart';
import 'package:uptet_saathi/models/content.dart';
import 'package:uptet_saathi/models/content_index.dart';
import 'package:uptet_saathi/models/revision.dart';
import 'package:uptet_saathi/repositories/content_repository.dart';
import 'package:uptet_saathi/repositories/progress_repository.dart';

import '../helpers.dart';

void main() {
  sqfliteFfiInit();

  late Directory dir;
  late String dbPath;
  late Database db;
  late ContentIndex content;
  late ProgressRepository progress;
  var now = DateTime(2026, 10, 26, 21);

  Future<void> open() async {
    db = await openAppDatabase(factory: databaseFactoryFfi, path: dbPath);
    final repo = ContentRepository(db);
    if (await repo.installedVersion() == null) {
      await repo.importPack(ContentPack.fromJson(samplePackJson()));
    }
    content = await repo.loadIndex();
    progress = ProgressRepository(db, clock: () => now);
  }

  setUp(() async {
    dir = await Directory.systemTemp.createTemp('uptet_test');
    dbPath = '${dir.path}/test.db';
    now = DateTime(2026, 10, 26, 21);
    await open();
  });

  tearDown(() async {
    await db.close();
    await dir.delete(recursive: true);
  });

  Future<int> startPaper() => progress.startAttempt(
        kind: AttemptKind.paper,
        paperId: 'p1',
        questions: content.questionsForPaper('p1'),
        marking: MarkingScheme.oneMarkNoNegative,
        contentVersion: content.contentVersion,
      );

  test('content is installed and indexed', () {
    expect(content.subjects.map((s) => s.id), ['s1']);
    expect(content.questionsForPaper('p1').map((q) => q.id), ['q1', 'q2']);
    expect(content.questionsForTopic('t1').map((q) => q.id), ['q1', 'q2']);
    expect(content.paperLanguages('p1'), {AppLanguage.en, AppLanguage.hi});
  });

  test('submitting scores the attempt and schedules wrong answers', () async {
    final id = await startPaper();
    await progress.saveAnswer(id, 'q1', 'A'); // correct
    await progress.saveAnswer(id, 'q2', 'B'); // wrong
    final attempt = await progress.submitAttempt(id, content);

    expect(attempt.isSubmitted, isTrue);
    expect(attempt.score, 1);
    expect(attempt.maxScore, 2);
    expect(attempt.correctCount, 1);
    expect(attempt.incorrectCount, 1);
    expect(attempt.unansweredCount, 0);
    expect(attempt.answers['q2']!.correctOptionId, 'A');
    expect(attempt.answers['q2']!.isCorrect, isFalse);

    final items = await progress.activeRevisionItems();
    expect(items.map((i) => i.questionId), ['q2']);
    expect(items.single.state.nextReviewAt, DateTime(2026, 10, 27));
    expect(await progress.dueRevisionItems(), isEmpty, reason: 'not due until tomorrow');
  });

  test('unanswered questions are not added to revision', () async {
    final id = await startPaper();
    await progress.saveAnswer(id, 'q1', 'A');
    final attempt = await progress.submitAttempt(id, content);
    expect(attempt.unansweredCount, 1);
    expect(await progress.activeRevisionItems(), isEmpty);
  });

  test('answers cannot change after submission and a second submit keeps the result', () async {
    final id = await startPaper();
    await progress.saveAnswer(id, 'q1', 'B');
    await progress.submitAttempt(id, content);
    expect(() => progress.saveAnswer(id, 'q1', 'A'), throwsStateError);
    final again = await progress.submitAttempt(id, content);
    expect(again.correctCount, 0);
  });

  test('progress survives closing and reopening the database', () async {
    final id = await startPaper();
    await progress.saveAnswer(id, 'q2', 'C');
    await progress.saveCurrentIndex(id, 1);
    await db.close();
    await open();

    final resumed = await progress.latestInProgress();
    expect(resumed!.id, id);
    expect(resumed.currentIndex, 1);
    expect(resumed.answers['q2']!.selectedOptionId, 'C');

    await progress.submitAttempt(id, content);
    await db.close();
    await open();
    final report = await progress.progressReport();
    expect(report.testsCompleted, 1);
    expect(report.incorrect, 1);
    expect(report.unanswered, 1);
    expect(report.revision.active, 1);
  });

  test('revision moves through the schedule to mastered without duplicates', () async {
    final id = await startPaper();
    await progress.saveAnswer(id, 'q2', 'B');
    await progress.submitAttempt(id, content);

    now = DateTime(2026, 10, 27, 8);
    var due = await progress.dueRevisionItems();
    expect(due, hasLength(1));
    var outcome = await progress.recordReview(due.single.id, 'A', content);
    expect(outcome.isCorrect, isTrue);
    expect(outcome.state.nextReviewAt, DateTime(2026, 10, 30));

    now = DateTime(2026, 10, 30, 8);
    due = await progress.dueRevisionItems();
    outcome = await progress.recordReview(due.single.id, 'A', content);
    expect(outcome.state.nextReviewAt, DateTime(2026, 11, 6));

    now = DateTime(2026, 11, 6, 8);
    due = await progress.dueRevisionItems();
    outcome = await progress.recordReview(due.single.id, 'A', content);
    expect(outcome.state.status, RevisionStatus.mastered);
    expect(await progress.activeRevisionItems(), isEmpty);

    // Wrong again in a later test: the same row comes back, no duplicate.
    final second = await startPaper();
    await progress.saveAnswer(second, 'q2', 'D');
    await progress.submitAttempt(second, content);
    final rows = await db.query('revision_items');
    expect(rows, hasLength(1));
    expect(rows.single['status'], 'active');
    expect(rows.single['source_attempt_id'], second);
    expect(await db.query('review_log'), hasLength(3));
  });

  test('a wrong review keeps the question in the queue', () async {
    final id = await startPaper();
    await progress.saveAnswer(id, 'q2', 'B');
    await progress.submitAttempt(id, content);
    now = DateTime(2026, 10, 27, 8);
    final item = (await progress.dueRevisionItems()).single;
    final outcome = await progress.recordReview(item.id, 'C', content);
    expect(outcome.isCorrect, isFalse);
    expect(outcome.state.stage, 0);
    expect(outcome.state.nextReviewAt, DateTime(2026, 10, 28));
    expect((await progress.revisionOverview()).active, 1);
  });

  test('discarding removes only unfinished attempts', () async {
    final done = await startPaper();
    await progress.submitAttempt(done, content);
    final open = await startPaper();
    await progress.discardInProgress(open);
    await progress.discardInProgress(done);
    expect(await progress.loadAttempt(open), isNull);
    expect(await progress.loadAttempt(done), isNotNull);
  });

  test('a content update retires removed questions without losing history', () async {
    final id = await startPaper();
    await progress.saveAnswer(id, 'q2', 'B');
    await progress.submitAttempt(id, content);

    final repo = ContentRepository(db);
    await repo.importPack(ContentPack.fromJson(samplePackJson(version: 'v2', questionIds: ['q1', 'q3'])));
    final updated = await repo.loadIndex();

    expect(updated.contentVersion, 'v2');
    expect(updated.questionsForPaper('p1').map((q) => q.id), ['q1']);
    expect(updated.question('q2'), isNotNull, reason: 'kept for past attempts');
    final attempt = await progress.loadAttempt(id);
    expect(attempt!.answers['q2']!.isCorrect, isFalse);

    // Importing the same pack twice is harmless.
    await repo.importPack(ContentPack.fromJson(samplePackJson(version: 'v2', questionIds: ['q1', 'q3'])));
    expect(await db.query('questions'), hasLength(3));
  });

  test('papers can share questions, and exam details are kept', () async {
    final json = samplePackJson(version: 'v2');
    final papers = json['papers'] as List;
    papers.add({
      ...papers.first as Map<String, Object?>,
      'id': 'p2',
      'exam': 'uptet',
      'level': 'junior',
      'question_ids': ['q1', 'q3'],
      'question_count': 2,
    });
    ((json['subjects'] as List).first as Map)['language'] = 'hi';
    final repo = ContentRepository(db);
    await repo.importPack(ContentPack.fromJson(json));
    final updated = await repo.loadIndex();

    expect(updated.questionsForPaper('p1').map((q) => q.id), ['q1', 'q2']);
    expect(updated.questionsForPaper('p2').map((q) => q.id), ['q1', 'q3']);
    expect(updated.paper('p2')!.exam, Exam.uptet);
    expect(updated.paper('p2')!.level, ExamLevel.junior);
    expect(updated.papersFor(Exam.uptet, ExamLevel.junior).map((p) => p.id), ['p2']);
    expect(updated.subject('s1')!.language, AppLanguage.hi);
  });

  test('progress report groups answers by topic', () async {
    for (var i = 0; i < 3; i++) {
      final id = await startPaper();
      await progress.saveAnswer(id, 'q1', 'B');
      await progress.saveAnswer(id, 'q2', 'B');
      await progress.submitAttempt(id, content);
    }
    final report = await progress.progressReport();
    expect(report.attempted, 6);
    expect(report.accuracyPercent, 0);
    expect(report.topics.single.topicId, 't1');
    expect(report.topics.single.answered, 6);
    expect(report.attempts, hasLength(3));
  });

  test('a mock test keeps its mode, time limit, clock and negative marking', () async {
    const settings = TestSettings(mode: AttemptMode.mock, timeLimitMinutes: 60, negativeMark: 0.25);
    final id = await progress.startAttempt(
      kind: AttemptKind.paper,
      paperId: 'p1',
      questions: content.questionsForPaper('p1'),
      marking: settings.markingFor(MarkingScheme.oneMarkNoNegative),
      contentVersion: content.contentVersion,
      mode: settings.mode,
      timeLimit: settings.timeLimitFor(150),
    );
    await progress.saveAnswer(id, 'q1', 'A');
    await progress.saveAnswer(id, 'q2', 'B');
    await progress.saveElapsed(id, const Duration(minutes: 12, seconds: 5));

    // Reopening the database keeps the clock for a resumed test.
    await db.close();
    await open();
    final resumed = (await progress.loadAttempt(id))!;
    expect(resumed.mode, AttemptMode.mock);
    expect(resumed.timeLimit, const Duration(minutes: 60));
    expect(resumed.elapsed, const Duration(minutes: 12, seconds: 5));

    final result = await progress.submitAttempt(id, content);
    expect(result.score, 0.75);
    expect(result.maxScore, 2);

    // The clock of a submitted attempt no longer moves.
    await progress.saveElapsed(id, const Duration(hours: 1));
    expect((await progress.loadAttempt(id))!.elapsed, const Duration(minutes: 12, seconds: 5));
  });

  test('practice attempts are untimed and use the paper marking', () async {
    final id = await startPaper();
    final attempt = (await progress.loadAttempt(id))!;
    expect(attempt.mode, AttemptMode.practice);
    expect(attempt.isTimed, isFalse);
    expect(attempt.elapsed, Duration.zero);
  });

  test('study activity counts first answers, reviews and time per day', () async {
    final id = await startPaper();
    await progress.saveAnswer(id, 'q1', 'A');
    await progress.saveAnswer(id, 'q1', 'B'); // a changed answer is not another question
    await progress.saveAnswer(id, 'q2', 'B');
    await progress.saveElapsed(id, const Duration(minutes: 5));
    await progress.saveElapsed(id, const Duration(minutes: 8));

    await progress.submitAttempt(id, content);
    now = DateTime(2026, 10, 27, 9);
    final due = await progress.dueRevisionItems();
    await progress.recordReview(due.first.id, 'A', content);

    final days = await progress.studyDays();
    expect(days.map((d) => (d.day, d.questions, d.seconds)), [
      (DateTime(2026, 10, 26), 2, 480),
      (DateTime(2026, 10, 27), 1, 0),
    ]);

    final report = await progress.progressReport();
    expect(report.papersCompleted, 1);
    expect(report.distinctQuestionsAttempted, 2);
    expect(report.studyDays, hasLength(2));
  });

  test('study activity survives a discarded attempt', () async {
    final id = await startPaper();
    await progress.saveAnswer(id, 'q1', 'A');
    await progress.discardInProgress(id);
    expect((await progress.studyDays()).single.questions, 1);
  });
}
