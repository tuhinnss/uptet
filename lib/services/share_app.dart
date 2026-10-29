import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../config.dart';
import '../l10n/strings.dart';

const _channel = MethodChannel('uptet_saathi/share');

/// Opens Android's share sheet with a short invitation and the Play Store link.
Future<void> shareApp(BuildContext context) async {
  final s = S.of(context);
  final messenger = ScaffoldMessenger.of(context);
  try {
    await _channel.invokeMethod<void>('shareText', {'title': s.shareApp, 'text': s.shareMessage(AppConfig.playStoreUrl)});
  } catch (e) {
    debugPrint('Could not share: $e');
    messenger.showSnackBar(SnackBar(content: Text(s.shareFailed)));
  }
}
