import 'package:flutter_test/flutter_test.dart';
import 'package:uptet_saathi/models/content.dart';
import 'package:uptet_saathi/services/feedback_link.dart';

void main() {
  const form = 'https://docs.google.com/forms/d/e/abc/viewform';

  test('no form configured means no link', () {
    expect(feedbackFormUri(contentVersion: 'v1', language: AppLanguage.hi, formUrl: ''), isNull);
  });

  test('only https forms are opened', () {
    expect(feedbackFormUri(contentVersion: 'v1', language: AppLanguage.hi, formUrl: 'http://example.com/form'), isNull);
  });

  test('without field IDs the plain form opens', () {
    final uri = feedbackFormUri(questionId: 'q1', contentVersion: 'v1', language: AppLanguage.hi, formUrl: form,
        questionField: '', contextField: '');
    expect(uri.toString(), form);
  });

  test('the reported question and installed content are prefilled', () {
    final uri = feedbackFormUri(
      questionId: 'q-uptet18-p-001',
      contentVersion: '2026.10.28-uptet.4',
      language: AppLanguage.en,
      formUrl: form,
      questionField: '111',
      contextField: '222',
    )!;
    expect(uri.path, '/forms/d/e/abc/viewform');
    expect(uri.queryParameters, {
      'usp': 'pp_url',
      'entry.111': 'q-uptet18-p-001',
      'entry.222': 'content 2026.10.28-uptet.4 · en',
    });
  });

  test('general feedback leaves the question field empty', () {
    final uri = feedbackFormUri(contentVersion: 'v1', language: AppLanguage.hi, formUrl: form,
        questionField: '111', contextField: '222')!;
    expect(uri.queryParameters.containsKey('entry.111'), isFalse);
    expect(uri.queryParameters['entry.222'], 'content v1 · hi');
  });
}
