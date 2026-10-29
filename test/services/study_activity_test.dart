import 'package:flutter_test/flutter_test.dart';
import 'package:uptet_saathi/services/study_activity.dart';

void main() {
  StudyDay day(int month, int d, {int questions = 1, int seconds = 0}) =>
      StudyDay(day: DateTime(2026, month, d), questions: questions, seconds: seconds);

  test('the current streak runs back from today', () {
    final s = streaksOf([day(10, 27), day(10, 28), day(10, 29)], DateTime(2026, 10, 29, 20));
    expect(s.current, 3);
    expect(s.best, 3);
  });

  test('the streak stays alive until today is over', () {
    final s = streaksOf([day(10, 27), day(10, 28)], DateTime(2026, 10, 29, 8));
    expect(s.current, 2);
  });

  test('a missed day ends the streak but keeps the best', () {
    final s = streaksOf([day(10, 20), day(10, 21), day(10, 22), day(10, 23), day(10, 26)], DateTime(2026, 10, 28));
    expect(s.current, 0);
    expect(s.best, 4);
  });

  test('streaks cross month ends', () {
    final s = streaksOf([day(9, 30), day(10, 1)], DateTime(2026, 10, 1));
    expect(s.current, 2);
  });

  test('a few seconds without answering does not count as a study day', () {
    expect(day(10, 1, questions: 0, seconds: 20).isActive, isFalse);
    expect(day(10, 1, questions: 0, seconds: 300).isActive, isTrue);
    expect(streaksOf([day(10, 29, questions: 0, seconds: 20)], DateTime(2026, 10, 29)).current, 0);
  });

  test('heat map shade grows with questions answered', () {
    expect(day(10, 1, questions: 0).level, -1);
    expect(day(10, 1, questions: 3).level, 0);
    expect(day(10, 1, questions: 30).level, 2);
    expect(day(10, 1, questions: 500).level, 4);
  });

  test('weekly time counts from Monday', () {
    // 29 Oct 2026 is a Thursday; the week began on Monday 26 Oct.
    final days = [day(10, 25, seconds: 3600), day(10, 26, seconds: 600), day(10, 29, seconds: 1200)];
    expect(timeThisWeek(days, DateTime(2026, 10, 29, 22)), const Duration(minutes: 30));
    expect(weekStart(DateTime(2026, 10, 26)), DateTime(2026, 10, 26));
  });

  test('day keys round-trip', () {
    expect(dayKey(DateTime(2026, 3, 7, 23, 59)), '2026-03-07');
    expect(parseDayKey('2026-03-07'), DateTime(2026, 3, 7));
  });
}
