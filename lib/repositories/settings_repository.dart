import 'dart:convert';

import 'package:sqflite/sqflite.dart';

import '../models/attempt.dart';
import '../models/content.dart';

class SettingsRepository {
  SettingsRepository(this._db);

  final Database _db;

  Future<AppLanguage?> language() async {
    final rows = await _db.query('settings', columns: ['value'], where: 'key = ?', whereArgs: ['language']);
    return rows.isEmpty ? null : AppLanguage.fromCode(rows.first['value'] as String);
  }

  Future<void> setLanguage(AppLanguage language) => _set('language', language.name);

  /// The settings used for the last paper, offered again for the next one.
  Future<TestSettings> testSettings() async {
    final rows = await _db.query('settings', columns: ['value'], where: 'key = ?', whereArgs: ['test_settings']);
    if (rows.isEmpty) return const TestSettings();
    try {
      return TestSettings.fromJson(jsonDecode(rows.first['value'] as String));
    } on FormatException {
      return const TestSettings();
    }
  }

  Future<void> setTestSettings(TestSettings settings) => _set('test_settings', jsonEncode(settings.toJson()));

  Future<void> _set(String key, String value) =>
      _db.insert('settings', {'key': key, 'value': value}, conflictAlgorithm: ConflictAlgorithm.replace);
}
