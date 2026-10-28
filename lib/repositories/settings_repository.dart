import 'package:sqflite/sqflite.dart';

import '../models/content.dart';

class SettingsRepository {
  SettingsRepository(this._db);

  final Database _db;

  Future<AppLanguage?> language() async {
    final rows = await _db.query('settings', columns: ['value'], where: 'key = ?', whereArgs: ['language']);
    return rows.isEmpty ? null : AppLanguage.fromCode(rows.first['value'] as String);
  }

  Future<void> setLanguage(AppLanguage language) => _db.insert(
        'settings',
        {'key': 'language', 'value': language.name},
        conflictAlgorithm: ConflictAlgorithm.replace,
      );
}
