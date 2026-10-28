import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:uptet_saathi/models/content.dart';
import 'package:uptet_saathi/services/bootstrap.dart';
import 'package:uptet_saathi/services/content_validator.dart';

import '../helpers.dart';

void main() {
  group('bundled content pack', () {
    final pack = ContentPack.fromJson(jsonDecode(File(contentPackAsset).readAsStringSync()));
    final issues = validateContentPack(pack, assetExists: (path) => File(path).existsSync());

    test('has no validation errors', () {
      expect(issues.where((i) => i.isError).map((i) => i.message), isEmpty);
    });

    // Papers whose source gives only one language; the other is still to be added.
    // CTET: Hindi still to be converted from the booklet's legacy font.
    const translationPendingPapers = {'ctet-feb26-p1-07feb-s'};

    test('every question is available in Hindi and English', () {
      final translationPending = {
        for (final p in pack.papers)
          if (translationPendingPapers.contains(p.id)) ...p.questionIds,
      };
      final languageSubjects = {
        for (final s in pack.subjects)
          if (s.language != null) s.id: s.language,
      };
      for (final q in pack.questions) {
        if (translationPending.contains(q.id)) continue;
        final fixed = languageSubjects[q.subjectId];
        expect(q.languages, fixed == null ? {AppLanguage.en, AppLanguage.hi} : contains(fixed), reason: q.id);
      }
    });

    test('paper question counts match the listed questions', () {
      for (final p in pack.papers) {
        expect(p.questionIds.length, p.questionCount, reason: p.id);
      }
    });

    test('is not presented as release-ready while questions are unverified', () {
      final allVerified = pack.questions.every((q) => q.verificationStatus == VerificationStatus.verified);
      if (pack.releaseReady) expect(allVerified, isTrue);
    });

    // An official paper comes from a checked source; its questions still go
    // through review during the pilot, but must all be verified for release.
    test('no release-ready paper is labelled official without verified questions', () {
      if (!pack.releaseReady) return;
      final byId = {for (final q in pack.questions) q.id: q};
      for (final p in pack.papers.where((p) => p.isOfficialPyq)) {
        for (final id in p.questionIds) {
          expect(byId[id]!.verificationStatus, VerificationStatus.verified, reason: '${p.id}/$id');
        }
      }
    });
  });

  group('validator', () {
    List<String> errorsFor(Map<String, Object?> json, {bool Function(String)? assetExists}) =>
        validateContentPack(ContentPack.fromJson(json), assetExists: assetExists)
            .where((i) => i.isError)
            .map((i) => i.message)
            .toList();

    test('accepts the sample pack', () {
      expect(errorsFor(samplePackJson()), isEmpty);
    });

    test('rejects a correct option that does not exist', () {
      final json = samplePackJson();
      ((json['questions'] as List).first as Map)['correct_option_id'] = 'E';
      expect(errorsFor(json), contains(contains('correct_option_id "E"')));
    });

    test('rejects duplicate question IDs', () {
      final json = samplePackJson();
      final questions = json['questions'] as List;
      questions.add(Map<String, Object?>.of(questions.first as Map<String, Object?>));
      expect(errorsFor(json), contains(contains('Duplicate question ID "q1"')));
    });

    test('rejects a question count that does not match', () {
      final json = samplePackJson();
      ((json['papers'] as List).first as Map)['question_count'] = 5;
      expect(errorsFor(json), contains(contains('question_count 5')));
    });

    test('rejects a topic from another subject', () {
      final json = samplePackJson();
      ((json['questions'] as List).first as Map)['subject_id'] = 'other';
      expect(errorsFor(json), contains(contains('does not belong to subject')));
    });

    test('rejects a missing option translation', () {
      final json = samplePackJson();
      final option = (((json['questions'] as List).first as Map)['options'] as List).first as Map;
      option['text'] = {'en': 'A'};
      expect(errorsFor(json), contains(contains('missing hi text')));
    });

    test('rejects unverified questions in a release-ready pack', () {
      final json = samplePackJson();
      ((json['questions'] as List).first as Map)['verification_status'] = 'pending_review';
      expect(errorsFor(json), contains(contains('not verified')));
    });

    test('rejects a paper without distribution permission in a release-ready pack', () {
      final json = samplePackJson();
      ((json['papers'] as List).first as Map)['distribution_cleared'] = false;
      expect(errorsFor(json), contains(contains('no recorded permission')));
    });

    test('only warns about missing distribution permission before release', () {
      final json = samplePackJson();
      json['release_ready'] = false;
      ((json['papers'] as List).first as Map)['distribution_cleared'] = false;
      expect(errorsFor(json), isEmpty);
    });

    test('accepts papers that share questions', () {
      final json = samplePackJson();
      final papers = json['papers'] as List;
      papers.add({...papers.first as Map<String, Object?>, 'id': 'p2'});
      expect(errorsFor(json), isEmpty);
    });

    test('rejects an official paper without an exam and level', () {
      final json = samplePackJson();
      final paper = (json['papers'] as List).first as Map;
      paper['is_official_pyq'] = true;
      paper['year'] = 2019;
      expect(errorsFor(json), contains(contains('no exam or level')));
      paper['exam'] = 'uptet';
      paper['level'] = 'junior';
      expect(errorsFor(json), isEmpty);
    });

    test('parsing reports an unknown exam', () {
      final json = samplePackJson();
      ((json['papers'] as List).first as Map)['exam'] = 'reet';
      expect(() => ContentPack.fromJson(json), throwsFormatException);
    });

    test('a language subject only needs its own language', () {
      final json = samplePackJson();
      final subject = (json['subjects'] as List).first as Map;
      subject['language'] = 'en';
      final q = (json['questions'] as List).first as Map;
      q['text'] = {'en': 'Pick the noun.'};
      q['options'] = [
        for (final o in ['A', 'B'])
          {
            'id': o,
            'text': {'en': o},
          },
      ];
      q['explanation'] = {'en': 'Because.'};
      final pack = ContentPack.fromJson(json);
      expect(errorsFor(json), isEmpty);
      expect(validateContentPack(pack).map((i) => i.message), isNot(contains(contains('"q1" has no hi'))));

      q['text'] = {'hi': 'संज्ञा चुनिए।'};
      expect(errorsFor(json), contains(contains('not written in en')));
    });

    test('rejects a missing PDF', () {
      final json = samplePackJson();
      ((json['papers'] as List).first as Map)['pdf_asset'] = 'assets/pdfs/missing.pdf';
      expect(errorsFor(json, assetExists: (_) => false), contains(contains('missing.pdf')));
    });

    test('parsing reports an unknown verification status', () {
      final json = samplePackJson();
      ((json['questions'] as List).first as Map)['verification_status'] = 'maybe';
      expect(() => ContentPack.fromJson(json), throwsFormatException);
    });
  });
}
