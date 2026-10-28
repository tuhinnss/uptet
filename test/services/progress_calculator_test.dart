import 'package:flutter_test/flutter_test.dart';
import 'package:uptet_saathi/services/progress_calculator.dart';

void main() {
  List<({String topicId, bool isCorrect})> answers(String topic, {required int correct, required int wrong}) => [
        for (var i = 0; i < correct; i++) (topicId: topic, isCorrect: true),
        for (var i = 0; i < wrong; i++) (topicId: topic, isCorrect: false),
      ];

  test('groups answers by topic', () {
    final result = topicPerformance([
      ...answers('a', correct: 3, wrong: 1),
      ...answers('b', correct: 0, wrong: 2),
    ]);
    final a = result.firstWhere((t) => t.topicId == 'a');
    expect(a.answered, 4);
    expect(a.correct, 3);
    expect(a.accuracyPercent, 75);
  });

  test('ignores topics with too few answers', () {
    final perf = topicPerformance(answers('a', correct: 0, wrong: 4));
    expect(weakTopics(perf, minAnswered: 5, belowAccuracy: 60), isEmpty);
  });

  test('flags topics below the accuracy threshold, weakest first', () {
    final perf = topicPerformance([
      ...answers('ok', correct: 4, wrong: 1),
      ...answers('weak', correct: 2, wrong: 3),
      ...answers('weaker', correct: 1, wrong: 5),
    ]);
    final weak = weakTopics(perf, minAnswered: 5, belowAccuracy: 60);
    expect(weak.map((t) => t.topicId), ['weaker', 'weak']);
  });

  test('a topic exactly at the threshold is not weak', () {
    final perf = topicPerformance(answers('edge', correct: 3, wrong: 2));
    expect(weakTopics(perf, minAnswered: 5, belowAccuracy: 60), isEmpty);
  });
}
