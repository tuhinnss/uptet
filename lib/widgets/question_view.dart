import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/content.dart';
import '../theme.dart';
import 'common.dart';
import 'option_tile.dart';

/// A question with its options. Before answers are revealed, options can be
/// selected; once [correctOptionId] is given, correctness and (optionally)
/// the explanation are shown.
class QuestionView extends StatelessWidget {
  const QuestionView({
    super.key,
    required this.question,
    required this.heading,
    required this.selectedOptionId,
    this.onSelect,
    this.correctOptionId,
    this.showExplanation = false,
    this.inlineHeading = false,
  });

  final Question question;
  final String heading;
  final String? selectedOptionId;
  final ValueChanged<String>? onSelect;
  final String? correctOptionId;
  final bool showExplanation;

  /// A short heading such as "Q21" set beside the question, as on the test screen.
  final bool inlineHeading;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final theme = Theme.of(context);
    final app = AppScope.of(context);
    final preferred = app.language;
    final language = question.displayLanguage(preferred);
    // Hindi and English language questions are meant to be in that language.
    final missingTranslation = language != preferred && app.content.subject(question.subjectId)?.language == null;
    final revealed = correctOptionId != null;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        if (!inlineHeading) Text(heading, style: theme.textTheme.labelLarge?.copyWith(color: theme.colorScheme.primary)),
        if (missingTranslation) ...[
          const SizedBox(height: 8),
          NoticeBanner(icon: Icons.translate, text: s.translationMissing),
        ],
        const SizedBox(height: 12),
        if (inlineHeading)
          Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(heading, style: const TextStyle(color: Colors.white, fontSize: 26, fontWeight: FontWeight.w700)),
              const SizedBox(width: 12),
              Expanded(
                child: Text(question.text.resolve(language).text,
                    style: const TextStyle(color: Colors.white, fontSize: 22, height: 1.45)),
              ),
            ],
          )
        else
          Text(
            question.text.resolve(language).text,
            style: theme.textTheme.titleMedium?.copyWith(height: 1.5),
          ),
        const SizedBox(height: 16),
        for (final option in question.options) ...[
          OptionTile(
            label: option.id,
            text: option.text.resolve(language).text,
            selected: option.id == selectedOptionId,
            reveal: !revealed
                ? OptionReveal.hidden
                : option.id == correctOptionId
                    ? OptionReveal.correct
                    : option.id == selectedOptionId
                        ? OptionReveal.wrong
                        : OptionReveal.neutral,
            onTap: onSelect == null ? null : () => onSelect!(option.id),
          ),
          const SizedBox(height: 12),
        ],
        if (revealed && selectedOptionId == null)
          Padding(
            padding: const EdgeInsets.only(bottom: 8),
            child: Text(s.youDidNotAnswer, style: theme.textTheme.bodyMedium?.copyWith(fontStyle: FontStyle.italic)),
          ),
        if (showExplanation && !question.explanation.isEmpty)
          Container(
            margin: const EdgeInsets.only(top: 4),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: AppColors.mint, borderRadius: BorderRadius.circular(16)),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(children: [
                  const Icon(Icons.lightbulb_outline, size: 20, color: AppColors.deepTeal),
                  const SizedBox(width: 6),
                  Text(s.explanation,
                      style: const TextStyle(color: AppColors.deepTeal, fontSize: 16, fontWeight: FontWeight.w700)),
                ]),
                const SizedBox(height: 6),
                Text(question.explanation.resolve(language).text,
                    style: const TextStyle(color: Colors.black87, fontSize: 16, height: 1.5)),
              ],
            ),
          ),
      ],
    );
  }
}
