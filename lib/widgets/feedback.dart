import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../services/feedback_link.dart';

/// Whether a feedback form is configured; the feedback buttons hide otherwise.
bool feedbackAvailable(AppController app) =>
    feedbackFormUri(contentVersion: app.content.contentVersion, language: app.language) != null;

/// Opens the feedback form in the browser, about [questionId] when given.
Future<void> openFeedbackForm(BuildContext context, {String? questionId}) async {
  final app = AppScope.read(context);
  final s = S.of(context);
  final messenger = ScaffoldMessenger.of(context);
  final uri = feedbackFormUri(questionId: questionId, contentVersion: app.content.contentVersion, language: app.language);
  var opened = false;
  if (uri != null) {
    try {
      opened = await launchUrl(uri, mode: LaunchMode.externalApplication);
    } catch (e) {
      debugPrint('Could not open feedback form: $e');
    }
  }
  if (!opened) messenger.showSnackBar(SnackBar(content: Text(s.feedbackOpenFailed)));
}

/// Small link under a reviewed question for reporting a mistake in it.
class ReportQuestionButton extends StatelessWidget {
  const ReportQuestionButton({super.key, required this.questionId});

  final String questionId;

  @override
  Widget build(BuildContext context) {
    if (!feedbackAvailable(AppScope.of(context))) return const SizedBox.shrink();
    return Align(
      alignment: Alignment.centerRight,
      child: TextButton.icon(
        icon: const Icon(Icons.flag_outlined, size: 18),
        label: Text(S.of(context).reportProblem),
        onPressed: () => openFeedbackForm(context, questionId: questionId),
      ),
    );
  }
}
