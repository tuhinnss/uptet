import 'package:flutter_test/flutter_test.dart';
import 'package:uptet_saathi/models/content.dart';
import 'package:uptet_saathi/services/scoring.dart';

import '../helpers.dart';

void main() {
  final questions = [
    question('q1', correct: 'A'),
    question('q2', correct: 'B'),
    question('q3', correct: 'C'),
    question('q4', correct: 'D'),
  ];

  test('counts correct, incorrect and unanswered separately', () {
    final result = scoreAnswers(
      questions: questions,
      selected: {'q1': 'A', 'q2': 'A', 'q3': null},
      marking: MarkingScheme.oneMarkNoNegative,
    );
    expect(result.correct, 1);
    expect(result.incorrect, 1);
    expect(result.unanswered, 2);
    expect(result.total, 4);
    expect(result.score, 1);
    expect(result.maxScore, 4);
  });

  test('accuracy uses answered questions only', () {
    final result = scoreAnswers(
      questions: questions,
      selected: {'q1': 'A', 'q2': 'A'},
      marking: MarkingScheme.oneMarkNoNegative,
    );
    expect(result.accuracyPercent, 50);
  });

  test('accuracy is null when nothing was answered', () {
    final result = scoreAnswers(questions: questions, selected: {}, marking: MarkingScheme.oneMarkNoNegative);
    expect(result.accuracyPercent, isNull);
    expect(result.score, 0);
  });

  test('applies negative marking', () {
    final result = scoreAnswers(
      questions: questions,
      selected: {'q1': 'A', 'q2': 'A', 'q3': 'A'},
      marking: const MarkingScheme(correct: 1, incorrect: -0.25),
    );
    expect(result.score, 0.5);
  });

  test('keeps question order and ignores answers to other questions', () {
    final result = scoreAnswers(
      questions: questions,
      selected: {'q4': 'D', 'other': 'A'},
      marking: MarkingScheme.oneMarkNoNegative,
    );
    expect(result.answers.map((a) => a.questionId), ['q1', 'q2', 'q3', 'q4']);
    expect(result.correct, 1);
  });

  test('is deterministic', () {
    ScoreResult run() => scoreAnswers(
          questions: questions,
          selected: {'q1': 'A', 'q2': 'C'},
          marking: MarkingScheme.oneMarkNoNegative,
        );
    expect(run().score, run().score);
    expect(run().correct, run().correct);
  });
}
