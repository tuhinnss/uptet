import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'package:sqflite/sqflite.dart';

import '../app_state.dart';
import '../database/app_database.dart';
import '../models/content.dart';
import '../repositories/content_repository.dart';
import '../repositories/progress_repository.dart';
import '../repositories/settings_repository.dart';
import 'content_validator.dart';

const contentPackAsset = 'assets/content/content_pack.json';

class ContentPackException implements Exception {
  ContentPackException(this.message);

  final String message;

  @override
  String toString() => message;
}

/// Opens the database, installs the bundled content pack when it is new, and
/// builds the [AppController].
///
/// A missing or invalid pack never replaces content that is already
/// installed; startup only fails when there is no usable content at all.
Future<AppController> bootstrap({
  AssetBundle? bundle,
  DatabaseFactory? databaseFactory,
  String? databasePath,
  DateTime Function()? clock,
}) async {
  final db = await openAppDatabase(factory: databaseFactory, path: databasePath);
  final contentRepository = ContentRepository(db);

  String? warning;
  try {
    final raw = await (bundle ?? rootBundle).loadString(contentPackAsset);
    final pack = ContentPack.fromJson(jsonDecode(raw));
    final errors = validateContentPack(pack).where((i) => i.isError).toList();
    if (errors.isNotEmpty) {
      throw ContentPackException('Content pack ${pack.contentVersion} is invalid:\n${errors.join('\n')}');
    }
    if (await contentRepository.installedVersion() != pack.contentVersion) {
      await contentRepository.importPack(pack);
    }
  } catch (e) {
    if (await contentRepository.installedVersion() == null) rethrow;
    debugPrint('Keeping previously installed content: $e');
    warning = e.toString();
  }

  Set<String> pdfs;
  try {
    final manifest = await AssetManifest.loadFromAssetBundle(bundle ?? rootBundle);
    pdfs = {for (final a in manifest.listAssets()) if (a.startsWith('assets/pdfs/')) a};
  } catch (e) {
    // Only the booklets named in the content pack are offered.
    debugPrint('Could not list bundled PDFs: $e');
    pdfs = const {};
  }

  final settings = SettingsRepository(db);
  return AppController(
    content: await contentRepository.loadIndex(),
    progress: ProgressRepository(db, clock: clock),
    settings: settings,
    language: await settings.language(),
    exam: await settings.exam(),
    contentWarning: warning,
    bundledPdfs: pdfs,
  );
}
