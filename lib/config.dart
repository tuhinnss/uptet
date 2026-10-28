/// Product rules that are MVP assumptions, kept in one place so they can be
/// tuned after the teacher pilot without hunting through the code.
class AppConfig {
  const AppConfig._();

  /// Days until each review: the next day, then 3 days later, then 7 days later.
  /// A question is mastered after one correct review per entry.
  static const List<int> revisionIntervalsDays = [1, 3, 7];

  /// A topic is only judged once at least this many of its questions were answered,
  /// so one or two unlucky answers don't label a topic as weak.
  static const int weakTopicMinAnswered = 5;

  /// Topics answered with accuracy below this percentage are flagged for practice.
  static const double weakTopicAccuracyThreshold = 60;
}
