import 'content.dart';

enum AttemptKind { paper, topic }

enum AttemptStatus {
  inProgress('in_progress'),
  submitted('submitted');

  const AttemptStatus(this.code);

  final String code;

  static AttemptStatus fromCode(String code) =>
      values.firstWhere((s) => s.code == code);
}

/// A learner's answer to one question of an attempt.
class AnswerRecord {
  const AnswerRecord({
    required this.questionId,
    this.selectedOptionId,
    this.correctOptionId,
    this.isCorrect,
  });

  final String questionId;
  final String? selectedOptionId;

  /// Answer key as it was at submission, so later corrections to the key
  /// don't rewrite past results. Null until the attempt is submitted.
  final String? correctOptionId;
  final bool? isCorrect;

  bool get isAnswered => selectedOptionId != null;
}

class Attempt {
  const Attempt({
    required this.id,
    required this.kind,
    required this.paperId,
    required this.topicId,
    required this.questionIds,
    required this.marking,
    required this.contentVersion,
    required this.status,
    required this.currentIndex,
    required this.startedAt,
    required this.updatedAt,
    required this.submittedAt,
    required this.score,
    required this.maxScore,
    required this.correctCount,
    required this.incorrectCount,
    required this.unansweredCount,
    required this.answers,
  });

  final int id;
  final AttemptKind kind;
  final String? paperId;
  final String? topicId;

  /// Question order fixed when the attempt started.
  final List<String> questionIds;
  final MarkingScheme marking;
  final String contentVersion;
  final AttemptStatus status;
  final int currentIndex;
  final DateTime startedAt;
  final DateTime updatedAt;
  final DateTime? submittedAt;
  final double? score;
  final double? maxScore;
  final int? correctCount;
  final int? incorrectCount;
  final int? unansweredCount;
  final Map<String, AnswerRecord> answers;

  bool get isSubmitted => status == AttemptStatus.submitted;
  int get totalQuestions => questionIds.length;
  int get answeredCount => answers.values.where((a) => a.isAnswered).length;

  /// Correct answers divided by answered questions, as a percentage.
  double? get accuracyPercent {
    final correct = correctCount, incorrect = incorrectCount;
    if (correct == null || incorrect == null || correct + incorrect == 0) return null;
    return correct * 100 / (correct + incorrect);
  }
}
