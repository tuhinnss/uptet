import 'package:flutter/material.dart';

import '../models/content.dart';

/// Icon for a subject card. Language subjects show a letter of their script.
Widget subjectIcon(Subject subject) {
  if (subject.id == 'san') return const _Letter('सं');
  if (subject.language case final language?) {
    return _Letter(language == AppLanguage.hi ? 'अ' : 'A');
  }
  return Icon(switch (subject.id) {
    'cdp' => Icons.child_care,
    'math' => Icons.square_foot,
    'evs' => Icons.eco_outlined,
    'sci' => Icons.science_outlined,
    'sst' => Icons.public,
    'gk' => Icons.lightbulb_outline,
    'life' => Icons.self_improvement,
    'reason' => Icons.psychology_outlined,
    'ict' => Icons.computer,
    _ => Icons.menu_book_outlined,
  });
}

class _Letter extends StatelessWidget {
  const _Letter(this.letter);

  final String letter;

  @override
  Widget build(BuildContext context) {
    final icon = IconTheme.of(context);
    final size = icon.size ?? 24;
    return SizedBox(
      width: size,
      height: size,
      child: Center(
        child: Text(letter,
            style: TextStyle(color: icon.color, fontSize: size * 0.8, fontWeight: FontWeight.w700, height: 1)),
      ),
    );
  }
}
