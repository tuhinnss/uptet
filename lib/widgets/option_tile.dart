import 'package:flutter/material.dart';

import '../l10n/strings.dart';
import 'common.dart';

/// How an option looks once answers are revealed.
enum OptionReveal { hidden, correct, wrong, neutral }

/// One answer option. Selection and correctness are shown with an icon and a
/// text label as well as colour.
class OptionTile extends StatelessWidget {
  const OptionTile({
    super.key,
    required this.label,
    required this.text,
    required this.selected,
    this.reveal = OptionReveal.hidden,
    this.onTap,
  });

  final String label;
  final String text;
  final bool selected;
  final OptionReveal reveal;
  final VoidCallback? onTap;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final theme = Theme.of(context);
    final scheme = theme.colorScheme;

    final (Color border, IconData icon, Color iconColor) = switch (reveal) {
      OptionReveal.correct => (FeedbackColors.correct(context), Icons.check_circle, FeedbackColors.correct(context)),
      OptionReveal.wrong => (FeedbackColors.wrong(context), Icons.cancel, FeedbackColors.wrong(context)),
      _ when selected => (scheme.primary, Icons.radio_button_checked, scheme.primary),
      _ => (scheme.outlineVariant, Icons.radio_button_unchecked, scheme.outline),
    };
    final tags = [
      if (selected && reveal != OptionReveal.hidden) s.yourAnswer,
      if (reveal == OptionReveal.correct) s.correctAnswer,
    ];

    return Semantics(
      selected: selected,
      button: onTap != null,
      child: Material(
        color: selected && reveal == OptionReveal.hidden ? scheme.primaryContainer.withValues(alpha: 0.5) : null,
        shape: RoundedRectangleBorder(
          side: BorderSide(color: border, width: selected || reveal == OptionReveal.correct ? 2 : 1),
          borderRadius: BorderRadius.circular(12),
        ),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: onTap,
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 14),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Icon(icon, color: iconColor),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('$label.  $text', style: theme.textTheme.bodyLarge?.copyWith(height: 1.5)),
                      if (tags.isNotEmpty)
                        Padding(
                          padding: const EdgeInsets.only(top: 4),
                          child: Text(
                            tags.join(' · '),
                            style: theme.textTheme.labelMedium?.copyWith(color: iconColor, fontWeight: FontWeight.bold),
                          ),
                        ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
