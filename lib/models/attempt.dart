import 'content.dart';

enum AttemptKind { paper, topic }

/// Practice is untimed; a mock test runs against a time limit like the real exam.
enum AttemptMode {
  practice,
  mock;

  static AttemptMode fromCode(String? code) => code == mock.name ? mock : practice;
}

/// Choices made before starting a paper. They are remembered as the default
/// for the next paper.
class TestSettings {
  const TestSettings({
    this.mode = AttemptMode.practice,
    this.timeLimitMinutes,
    this.negativeMark = 0,
    this.shuffle = false,
  });

  final AttemptMode mode;

  /// Mock test time; null means the paper's full time.
  final int? timeLimitMinutes;

  /// Marks taken off per wrong answer in a mock test, as a positive number.
  final double negativeMark;
  final bool shuffle;

  static const negativeMarkChoices = [0.0, 0.25, 1 / 3, 0.5, 1.0];
  static const timeLimitChoices = [120, 90, 60, 30];

  /// Time limit for a paper whose full time is [fullMinutes]; null for practice.
  Duration? timeLimitFor(int fullMinutes) =>
      mode == AttemptMode.mock ? Duration(minutes: timeLimitMinutes ?? fullMinutes) : null;

  /// The paper's marking, with this mock test's negative marking applied.
  MarkingScheme markingFor(MarkingScheme paper) => mode == AttemptMode.mock
      ? MarkingScheme(correct: paper.correct, incorrect: -negativeMark, unanswered: paper.unanswered)
      : paper;

  TestSettings copyWith({AttemptMode? mode, int? Function()? timeLimitMinutes, double? negativeMark, bool? shuffle}) =>
      TestSettings(
        mode: mode ?? this.mode,
        timeLimitMinutes: timeLimitMinutes != null ? timeLimitMinutes() : this.timeLimitMinutes,
        negativeMark: negativeMark ?? this.negativeMark,
        shuffle: shuffle ?? this.shuffle,
      );

  Map<String, Object?> toJson() =>
      {'mode': mode.name, 'time_limit_minutes': timeLimitMinutes, 'negative_mark': negativeMark, 'shuffle': shuffle};

  /// Falls back to defaults for anything missing or malformed, so a bad saved
  /// value never stops a test from starting.
  factory TestSettings.fromJson(Object? json) {
    if (json is! Map) return const TestSettings();
    final minutes = json['time_limit_minutes'];
    final negative = json['negative_mark'];
    return TestSettings(
      mode: AttemptMode.fromCode(json['mode'] as String?),
      timeLimitMinutes: minutes is int && minutes > 0 ? minutes : null,
      negativeMark: negative is num && negative >= 0 ? negative.toDouble() : 0,
      shuffle: json['shuffle'] == true,
    );
  }
}

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
    this.mode = AttemptMode.practice,
    this.timeLimit,
    this.elapsed = Duration.zero,
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
  final AttemptMode mode;

  /// Set for a mock test.
  final Duration? timeLimit;

  /// Time spent with the test open. The clock stops while the learner is away.
  final Duration elapsed;
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
  bool get isTimed => timeLimit != null;
  int get totalQuestions => questionIds.length;
  int get answeredCount => answers.values.where((a) => a.isAnswered).length;

  /// Correct answers divided by answered questions, as a percentage.
  double? get accuracyPercent {
    final correct = correctCount, incorrect = incorrectCount;
    if (correct == null || incorrect == null || correct + incorrect == 0) return null;
    return correct * 100 / (correct + incorrect);
  }
}
