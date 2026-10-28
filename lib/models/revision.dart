enum RevisionStatus {
  active,
  mastered;

  static RevisionStatus fromCode(String code) =>
      values.firstWhere((s) => s.name == code);
}

/// Where a question stands in the revision sequence.
class RevisionState {
  const RevisionState({
    required this.stage,
    required this.status,
    required this.nextReviewAt,
    required this.consecutiveCorrect,
    this.lastReviewedAt,
  });

  /// Number of successful reviews so far in the current sequence.
  final int stage;
  final RevisionStatus status;

  /// Local midnight of the day the question becomes due.
  final DateTime nextReviewAt;
  final DateTime? lastReviewedAt;
  final int consecutiveCorrect;

  bool isDue(DateTime now) =>
      status == RevisionStatus.active && !nextReviewAt.isAfter(now);
}

class RevisionItem {
  const RevisionItem({
    required this.id,
    required this.questionId,
    required this.sourceAttemptId,
    required this.state,
    required this.createdAt,
  });

  final int id;
  final String questionId;
  final int? sourceAttemptId;
  final RevisionState state;
  final DateTime createdAt;
}
