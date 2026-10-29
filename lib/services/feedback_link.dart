import '../config.dart';
import '../models/content.dart';

/// Link to the pilot feedback form, prefilled with the reported question and
/// the installed content, so a report can be traced without the learner typing
/// IDs. Null when no form is configured.
Uri? feedbackFormUri({
  String? questionId,
  required String contentVersion,
  required AppLanguage language,
  String formUrl = AppConfig.feedbackFormUrl,
  String questionField = AppConfig.feedbackQuestionField,
  String contextField = AppConfig.feedbackContextField,
}) {
  if (formUrl.isEmpty) return null;
  final base = Uri.tryParse(formUrl);
  if (base == null || base.scheme != 'https') return null;
  final prefill = {
    if (questionField.isNotEmpty && questionId != null) 'entry.$questionField': questionId,
    if (contextField.isNotEmpty) 'entry.$contextField': 'content $contentVersion · ${language.name}',
  };
  if (prefill.isEmpty) return base;
  return base.replace(queryParameters: {...base.queryParameters, 'usp': 'pp_url', ...prefill});
}
