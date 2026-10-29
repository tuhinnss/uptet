import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/content.dart';
import '../services/share_app.dart';
import 'feedback.dart';

/// App-bar button showing the current language; opens the settings sheet.
class LanguageButton extends StatelessWidget {
  const LanguageButton({super.key});

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    return TextButton.icon(
      onPressed: () => showSettingsSheet(context),
      icon: const Icon(Icons.translate),
      label: Text(app.language == AppLanguage.hi ? 'हिन्दी' : 'EN'),
    );
  }
}

Future<void> showSettingsSheet(BuildContext context) => showModalBottomSheet<void>(
      context: context,
      showDragHandle: true,
      isScrollControlled: true,
      builder: (_) => const _SettingsSheet(),
    );

class _SettingsSheet extends StatelessWidget {
  const _SettingsSheet();

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    final s = S.of(context);
    final theme = Theme.of(context);
    return SafeArea(
      child: SingleChildScrollView(
        padding: const EdgeInsets.fromLTRB(20, 0, 20, 20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(s.language, style: theme.textTheme.titleMedium),
            const SizedBox(height: 12),
            SegmentedButton<AppLanguage>(
              segments: [
                for (final l in [AppLanguage.hi, AppLanguage.en])
                  ButtonSegment(value: l, label: Text(s.languageName(l))),
              ],
              selected: {app.language},
              onSelectionChanged: (selection) => app.setLanguage(selection.first),
            ),
            const SizedBox(height: 12),
            ListTile(
              contentPadding: EdgeInsets.zero,
              leading: const Icon(Icons.share_outlined),
              title: Text(s.shareApp),
              subtitle: Text(s.shareAppSubtitle),
              onTap: () => shareApp(context),
            ),
            if (feedbackAvailable(app)) ...[
              const SizedBox(height: 20),
              ListTile(
                contentPadding: EdgeInsets.zero,
                leading: const Icon(Icons.feedback_outlined),
                title: Text(s.sendFeedback),
                subtitle: Text(s.feedbackHint),
                trailing: const Icon(Icons.open_in_new),
                onTap: () => openFeedbackForm(context),
              ),
            ],
            const SizedBox(height: 28),
            Text(s.aboutDataTitle, style: theme.textTheme.titleMedium),
            const SizedBox(height: 8),
            Text(s.aboutDataBody, style: theme.textTheme.bodyMedium?.copyWith(height: 1.5)),
            const SizedBox(height: 20),
            Text('${s.contentVersionLabel}: ${app.content.contentVersion}', style: theme.textTheme.bodySmall),
          ],
        ),
      ),
    );
  }
}
