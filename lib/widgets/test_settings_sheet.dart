import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/attempt.dart';
import '../models/content.dart';
import 'common.dart';

/// Asks how to take a paper: untimed practice or a mock test. A mock test
/// always runs like the real exam, with the paper's full time and marking.
/// Returns null when dismissed. The choice is saved as the default for the next paper.
Future<TestSettings?> showTestSettingsSheet(BuildContext context,
    {required int fullMinutes, required MarkingScheme marking}) async {
  final app = AppScope.read(context);
  TestSettings initial;
  try {
    initial = await app.settings.testSettings();
  } catch (e) {
    debugPrint('Could not read test settings: $e');
    initial = const TestSettings();
  }
  if (!context.mounted) return null;
  final chosen = await showModalBottomSheet<TestSettings>(
    context: context,
    showDragHandle: true,
    isScrollControlled: true,
    builder: (_) => _TestSettingsSheet(initial: initial, fullMinutes: fullMinutes, marking: marking),
  );
  if (chosen != null) {
    try {
      await app.settings.setTestSettings(chosen);
    } catch (e) {
      // Only the remembered default is lost; the test still starts with these settings.
      debugPrint('Could not save test settings: $e');
    }
  }
  return chosen;
}

class _TestSettingsSheet extends StatefulWidget {
  const _TestSettingsSheet({required this.initial, required this.fullMinutes, required this.marking});

  final TestSettings initial;
  final int fullMinutes;
  final MarkingScheme marking;

  @override
  State<_TestSettingsSheet> createState() => _TestSettingsSheetState();
}

class _TestSettingsSheetState extends State<_TestSettingsSheet> {
  // Time limits and negative marking chosen in earlier versions no longer apply.
  late TestSettings _settings = widget.initial.copyWith(timeLimitMinutes: () => null, negativeMark: 0);

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final theme = Theme.of(context);
    final mock = _settings.mode == AttemptMode.mock;

    return SafeArea(
      child: SingleChildScrollView(
        padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(s.testSettings, style: theme.textTheme.titleLarge),
            const SizedBox(height: 16),
            SegmentedButton<AttemptMode>(
              segments: [
                ButtonSegment(value: AttemptMode.practice, icon: const Icon(Icons.menu_book), label: Text(s.modePractice)),
                ButtonSegment(value: AttemptMode.mock, icon: const Icon(Icons.timer_outlined), label: Text(s.modeMock)),
              ],
              selected: {_settings.mode},
              onSelectionChanged: (selection) => setState(() => _settings = _settings.copyWith(mode: selection.first)),
            ),
            const SizedBox(height: 8),
            Text(mock ? s.mockModeHint : s.practiceModeHint, style: theme.textTheme.bodySmall),
            if (mock) ...[
              const SizedBox(height: 16),
              Wrap(spacing: 8, runSpacing: 8, children: [
                InfoChip(icon: Icons.timer_outlined, label: s.fullTime(widget.fullMinutes)),
                InfoChip(icon: Icons.rule, label: s.marking(widget.marking)),
              ]),
            ],
            const SizedBox(height: 12),
            SwitchListTile(
              contentPadding: EdgeInsets.zero,
              title: Text(s.shuffleQuestions),
              value: _settings.shuffle,
              onChanged: (value) => setState(() => _settings = _settings.copyWith(shuffle: value)),
            ),
            const SizedBox(height: 12),
            FilledButton.icon(
              style: FilledButton.styleFrom(minimumSize: const Size.fromHeight(52)),
              icon: const Icon(Icons.play_arrow),
              label: Text(s.startTest),
              onPressed: () => Navigator.pop(context, _settings),
            ),
          ],
        ),
      ),
    );
  }
}
