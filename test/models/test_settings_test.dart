import 'package:flutter_test/flutter_test.dart';
import 'package:uptet_saathi/models/attempt.dart';
import 'package:uptet_saathi/models/content.dart';

void main() {
  const paper = MarkingScheme(correct: 1);

  test('practice is untimed and keeps the paper marking', () {
    const settings = TestSettings(negativeMark: 0.25, timeLimitMinutes: 60);
    expect(settings.timeLimitFor(150), isNull);
    expect(settings.markingFor(paper).incorrect, 0);
  });

  test('a mock test uses the chosen time, or the full time', () {
    expect(const TestSettings(mode: AttemptMode.mock, timeLimitMinutes: 60).timeLimitFor(150),
        const Duration(minutes: 60));
    expect(const TestSettings(mode: AttemptMode.mock).timeLimitFor(150), const Duration(minutes: 150));
  });

  test('a mock test applies negative marking as a deduction', () {
    final marking = const TestSettings(mode: AttemptMode.mock, negativeMark: 0.25).markingFor(paper);
    expect(marking.correct, 1);
    expect(marking.incorrect, -0.25);
  });

  test('settings survive a JSON round trip', () {
    const settings = TestSettings(mode: AttemptMode.mock, timeLimitMinutes: 90, negativeMark: 1 / 3, shuffle: true);
    final back = TestSettings.fromJson(settings.toJson());
    expect(back.mode, AttemptMode.mock);
    expect(back.timeLimitMinutes, 90);
    expect(back.negativeMark, closeTo(1 / 3, 1e-9));
    expect(back.shuffle, isTrue);
  });

  test('malformed saved settings fall back to defaults', () {
    final back = TestSettings.fromJson({'mode': 'exam', 'time_limit_minutes': -5, 'negative_mark': 'x'});
    expect(back.mode, AttemptMode.practice);
    expect(back.timeLimitMinutes, isNull);
    expect(back.negativeMark, 0);
    expect(TestSettings.fromJson(null).mode, AttemptMode.practice);
  });
}
