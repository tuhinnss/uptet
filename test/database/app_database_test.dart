import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:sqflite_common_ffi/sqflite_ffi.dart';
import 'package:uptet_saathi/database/app_database.dart';
import 'package:uptet_saathi/repositories/content_repository.dart';

void main() {
  sqfliteFfiInit();

  test('upgrading a version 1 database keeps existing rows', () async {
    final dir = await Directory.systemTemp.createTemp('uptet_migration');
    final path = '${dir.path}/test.db';

    final v1 = await databaseFactoryFfi.openDatabase(
      path,
      options: OpenDatabaseOptions(
        version: 1,
        onCreate: (db, _) async {
          for (final sql in migrations[0]) {
            await db.execute(sql);
          }
        },
      ),
    );
    await v1.insert('settings', {'key': 'language', 'value': 'hi'});
    await v1.insert('subjects', {'subject_id': 's1', 'sort_order': 0});
    await v1.insert('topics', {'topic_id': 't1', 'subject_id': 's1', 'sort_order': 0});
    await v1.insert('papers', {
      'paper_id': 'p1',
      'is_official_pyq': 0,
      'language_availability': 'en,hi',
      'marking_scheme_json': '{"correct":1}',
      'question_count': 2,
      'source_reference': 'test',
      'sort_order': 0,
      'content_version': 'v1',
    });
    for (final (position, id) in [(1, 'q2'), (0, 'q1')]) {
      await v1.insert('questions', {
        'question_id': id,
        'paper_id': 'p1',
        'paper_position': position,
        'subject_id': 's1',
        'topic_id': 't1',
        'question_text_en': 'Question $id',
        'options_json': '[{"id":"A","en":"A"},{"id":"B","en":"B"}]',
        'correct_option_id': 'A',
        'source_reference': 'test',
        'verification_status': 'verified',
        'sort_order': position,
        'content_version': 'v1',
      });
    }
    await v1.close();

    final db = await openAppDatabase(factory: databaseFactoryFfi, path: path);
    expect(await db.getVersion(), schemaVersion);
    expect(await db.query('settings'), [
      {'key': 'language', 'value': 'hi'},
    ]);
    final papers = await db.query('papers');
    expect(papers.single['paper_id'], 'p1');
    expect(papers.single['distribution_cleared'], 0);
    expect(papers.single['question_ids_json'], isNull);

    // A paper installed before papers kept their own question list.
    final content = await ContentRepository(db).loadIndex();
    expect(content.paper('p1')!.questionIds, ['q1', 'q2']);
    expect(content.paper('p1')!.exam, isNull);

    await db.close();
    await dir.delete(recursive: true);
  });
}
