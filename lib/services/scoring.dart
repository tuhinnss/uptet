import '../models/content.dart';

class ScoredAnswer {
  const ScoredAnswer({
    required this.questionId,
    required this.selectedOptionId,
    required this.correctOptionId,
  });

  final String questionId;
  final String? selectedOptionId;
  final String correctOptionId;

  bool get isAnswered => selectedOptionId != null;
  bool get isCorrect => isAnswered && selectedOptionId == correctOptionId;
}

class ScoreResult {
  const ScoreResult({required this.answers, required this.score, required this.maxScore});

  final List<ScoredAnswer> answers;
  final double score;
  final double maxScore;

  int get total => answers.length;
  int get correct => answers.where((a) => a.isCorrect).length;
  int get incorrect => answers.where((a) => a.isAnswered && !a.isCorrect).length;
  int get unanswered => answers.where((a) => !a.isAnswered).length;
  double? get accuracyPercent => accuracyPercentOf(correct, correct + incorrect);
}

/// Scores [questions] in order against [selected] (question ID → option ID).
/// Deterministic: the same inputs always give the same result.
ScoreResult scoreAnswers({
  required List<Question> questions,
  required Map<String, String?> selected,
  required MarkingScheme marking,
}) {
  final answers = [
    for (final q in questions)
      ScoredAnswer(
        questionId: q.id,
        selectedOptionId: selected[q.id],
        correctOptionId: q.correctOptionId,
      ),
  ];
  var score = 0.0;
  for (final a in answers) {
    score += !a.isAnswered
        ? marking.unanswered
        : a.isCorrect
            ? marking.correct
            : marking.incorrect;
  }
  return ScoreResult(answers: answers, score: score, maxScore: marking.correct * answers.length);
}

/// Correct answers divided by answered questions × 100; null when nothing was answered.
double? accuracyPercentOf(int correct, int answered) =>
    answered == 0 ? null : correct * 100 / answered;
