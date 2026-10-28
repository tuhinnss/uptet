import '../config.dart';

class TopicPerformance {
  const TopicPerformance({required this.topicId, required this.answered, required this.correct});

  final String topicId;
  final int answered;
  final int correct;

  double get accuracyPercent => answered == 0 ? 0 : correct * 100 / answered;
}

/// Groups answered questions by topic. Unanswered questions are not passed in.
List<TopicPerformance> topicPerformance(Iterable<({String topicId, bool isCorrect})> answers) {
  final answered = <String, int>{};
  final correct = <String, int>{};
  for (final a in answers) {
    answered.update(a.topicId, (n) => n + 1, ifAbsent: () => 1);
    if (a.isCorrect) correct.update(a.topicId, (n) => n + 1, ifAbsent: () => 1);
  }
  return [
    for (final MapEntry(key: topicId, value: count) in answered.entries)
      TopicPerformance(topicId: topicId, answered: count, correct: correct[topicId] ?? 0),
  ]..sort((a, b) => a.accuracyPercent.compareTo(b.accuracyPercent));
}

/// Topics with enough answers to judge and accuracy below the threshold,
/// weakest first.
List<TopicPerformance> weakTopics(
  List<TopicPerformance> performance, {
  int minAnswered = AppConfig.weakTopicMinAnswered,
  double belowAccuracy = AppConfig.weakTopicAccuracyThreshold,
}) =>
    performance
        .where((p) => p.answered >= minAnswered && p.accuracyPercent < belowAccuracy)
        .toList()
      ..sort((a, b) => a.accuracyPercent.compareTo(b.accuracyPercent));
