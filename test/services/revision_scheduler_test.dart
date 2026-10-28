import 'package:flutter_test/flutter_test.dart';
import 'package:uptet_saathi/models/revision.dart';
import 'package:uptet_saathi/services/revision_scheduler.dart';

void main() {
  const scheduler = RevisionScheduler(intervalsDays: [1, 3, 7]);
  final monday9pm = DateTime(2026, 10, 26, 21, 0);

  test('a wrong test answer is due at the start of the next day', () {
    final state = scheduler.afterIncorrectInTest(monday9pm);
    expect(state.stage, 0);
    expect(state.status, RevisionStatus.active);
    expect(state.nextReviewAt, DateTime(2026, 10, 27));
    expect(state.isDue(DateTime(2026, 10, 26, 23, 59)), isFalse);
    expect(state.isDue(DateTime(2026, 10, 27, 0, 0)), isTrue);
  });

  test('correct reviews follow next day, +3 days, +7 days, then mastered', () {
    var state = scheduler.afterIncorrectInTest(monday9pm);
    final day1 = DateTime(2026, 10, 27, 8);
    state = scheduler.afterReview(state, correct: true, now: day1);
    expect(state.stage, 1);
    expect(state.nextReviewAt, DateTime(2026, 10, 30));

    final day4 = DateTime(2026, 10, 30, 19);
    state = scheduler.afterReview(state, correct: true, now: day4);
    expect(state.stage, 2);
    expect(state.nextReviewAt, DateTime(2026, 11, 6));

    final day11 = DateTime(2026, 11, 6, 7);
    state = scheduler.afterReview(state, correct: true, now: day11);
    expect(state.status, RevisionStatus.mastered);
    expect(state.consecutiveCorrect, 3);
    expect(state.isDue(DateTime(2030)), isFalse);
  });

  test('a wrong review restarts the sequence and stays in the queue', () {
    var state = scheduler.afterIncorrectInTest(monday9pm);
    state = scheduler.afterReview(state, correct: true, now: DateTime(2026, 10, 27, 8));
    state = scheduler.afterReview(state, correct: false, now: DateTime(2026, 10, 30, 8));
    expect(state.stage, 0);
    expect(state.status, RevisionStatus.active);
    expect(state.consecutiveCorrect, 0);
    expect(state.nextReviewAt, DateTime(2026, 10, 31));
    expect(state.lastReviewedAt, DateTime(2026, 10, 30, 8));
  });

  test('a mastered question re-enters revision after a wrong test answer', () {
    final mastered = RevisionState(
      stage: 3,
      status: RevisionStatus.mastered,
      nextReviewAt: DateTime(2026, 10, 1),
      lastReviewedAt: DateTime(2026, 10, 1),
      consecutiveCorrect: 3,
    );
    final state = scheduler.afterIncorrectInTest(monday9pm, current: mastered);
    expect(state.status, RevisionStatus.active);
    expect(state.stage, 0);
    expect(state.lastReviewedAt, DateTime(2026, 10, 1));
  });

  test('due dates use calendar days across month ends', () {
    expect(dueDay(DateTime(2026, 12, 31, 23, 30), 1), DateTime(2027, 1, 1));
    expect(dueDay(DateTime(2026, 2, 26, 10), 7), DateTime(2026, 3, 5));
  });

  test('calendarDaysBetween counts local dates, not 24-hour periods', () {
    expect(calendarDaysBetween(DateTime(2026, 10, 26, 23, 59), DateTime(2026, 10, 27)), 1);
    expect(calendarDaysBetween(DateTime(2026, 10, 27, 8), DateTime(2026, 10, 30)), 3);
  });
}
