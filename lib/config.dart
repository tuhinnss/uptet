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

  /// Google Form for pilot feedback (its "viewform" link). While empty, the
  /// feedback buttons are hidden. Can also be set at build time:
  /// `flutter build apk --dart-define=FEEDBACK_FORM_URL=https://docs.google.com/forms/d/e/.../viewform`
  static const String feedbackFormUrl = String.fromEnvironment('FEEDBACK_FORM_URL');

  /// IDs of the form's short-answer fields that are filled in for the
  /// learner, from the form's "Get pre-filled link" (the number in `entry.123`).
  /// Empty leaves that field for the learner to fill in.
  static const String feedbackQuestionField = String.fromEnvironment('FEEDBACK_QUESTION_FIELD');
  static const String feedbackContextField = String.fromEnvironment('FEEDBACK_CONTEXT_FIELD');
}
