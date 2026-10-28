import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/content.dart';

/// First launch: the learner picks the interface language before anything else.
class LanguageChoiceScreen extends StatelessWidget {
  const LanguageChoiceScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final app = AppScope.read(context);
    final theme = Theme.of(context);
    return Scaffold(
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(24),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Icon(Icons.menu_book_rounded, size: 56, color: theme.colorScheme.primary),
                const SizedBox(height: 12),
                Text('UPTET साथी · UPTET Saathi',
                    textAlign: TextAlign.center, style: theme.textTheme.headlineSmall),
                const SizedBox(height: 32),
                Text(S.chooseLanguageTitle, textAlign: TextAlign.center, style: theme.textTheme.titleMedium),
                const SizedBox(height: 24),
                FilledButton(
                  style: FilledButton.styleFrom(minimumSize: const Size.fromHeight(56)),
                  onPressed: () => app.setLanguage(AppLanguage.hi),
                  child: const Text('हिन्दी', style: TextStyle(fontSize: 18)),
                ),
                const SizedBox(height: 12),
                FilledButton.tonal(
                  style: FilledButton.styleFrom(minimumSize: const Size.fromHeight(56)),
                  onPressed: () => app.setLanguage(AppLanguage.en),
                  child: const Text('English', style: TextStyle(fontSize: 18)),
                ),
                const SizedBox(height: 24),
                Text(S.chooseLanguageHint, textAlign: TextAlign.center, style: theme.textTheme.bodySmall),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
