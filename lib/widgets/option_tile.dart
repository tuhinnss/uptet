import 'package:flutter/material.dart';

import '../l10n/strings.dart';
import '../theme.dart';

/// How an option looks once answers are revealed.
enum OptionReveal { hidden, correct, wrong, neutral }

/// One answer option on a white card: "A)" in teal, then the text. Selection
/// and correctness are shown with an icon and a text label as well as colour.
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
    final (Color background, Color? border, IconData? icon, Color accent) = switch (reveal) {
      OptionReveal.correct => (const Color(0xFFDDF5E1), AppColors.correct, Icons.check_circle, AppColors.correct),
      OptionReveal.wrong => (const Color(0xFFFBE2E2), AppColors.wrong, Icons.cancel, AppColors.wrong),
      _ when selected => (AppColors.mint, AppColors.deepTeal, Icons.radio_button_checked, AppColors.deepTeal),
      _ => (Colors.white, null, null, AppColors.accentTeal),
    };
    final tags = [
      if (selected && reveal != OptionReveal.hidden) s.yourAnswer,
      if (reveal == OptionReveal.correct) s.correctAnswer,
    ];

    return Semantics(
      selected: selected,
      button: onTap != null,
      child: Material(
        color: background,
        shape: RoundedRectangleBorder(
          side: border == null ? BorderSide.none : BorderSide(color: border, width: 3),
          borderRadius: BorderRadius.circular(22),
        ),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: onTap,
          child: Padding(
            padding: const EdgeInsets.fromLTRB(18, 14, 14, 14),
            child: Row(
              children: [
                Text('$label)', style: TextStyle(color: accent, fontSize: 28, fontWeight: FontWeight.w700)),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(text, style: const TextStyle(color: Colors.black, fontSize: 19, height: 1.4)),
                      if (tags.isNotEmpty)
                        Padding(
                          padding: const EdgeInsets.only(top: 4),
                          child: Text(
                            tags.join(' · '),
                            style: TextStyle(color: accent, fontSize: 13, fontWeight: FontWeight.w700),
                          ),
                        ),
                    ],
                  ),
                ),
                if (icon != null) ...[const SizedBox(width: 8), Icon(icon, color: accent)],
              ],
            ),
          ),
        ),
      ),
    );
  }
}
