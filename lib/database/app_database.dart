import 'package:path/path.dart' as p;
import 'package:sqflite/sqflite.dart';

const databaseFileName = 'uptet_saathi.db';

/// Schema migrations: entry `i` upgrades the database from version `i` to `i + 1`.
///
/// Never edit a migration that has shipped; append a new one so learners keep
/// their progress through app updates. SQL avoids UPSERT and other features
/// missing from the SQLite bundled with older Android versions.
const List<List<String>> migrations = [
  // v1
  [
    'CREATE TABLE settings (key TEXT PRIMARY KEY, value TEXT NOT NULL)',
    'CREATE TABLE content_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL)',
    '''CREATE TABLE subjects (
      subject_id TEXT PRIMARY KEY,
      name_en TEXT,
      name_hi TEXT,
      sort_order INTEGER NOT NULL,
      is_active INTEGER NOT NULL DEFAULT 1
    )''',
    '''CREATE TABLE topics (
      topic_id TEXT PRIMARY KEY,
      subject_id TEXT NOT NULL REFERENCES subjects (subject_id),
      name_en TEXT,
      name_hi TEXT,
      sort_order INTEGER NOT NULL,
      is_active INTEGER NOT NULL DEFAULT 1
    )''',
    '''CREATE TABLE papers (
      paper_id TEXT PRIMARY KEY,
      title_en TEXT,
      title_hi TEXT,
      year INTEGER,
      paper_code TEXT,
      is_official_pyq INTEGER NOT NULL,
      language_availability TEXT NOT NULL,
      duration_minutes INTEGER,
      marking_scheme_json TEXT NOT NULL,
      pdf_asset_path TEXT,
      question_count INTEGER NOT NULL,
      source_reference TEXT NOT NULL,
      sort_order INTEGER NOT NULL,
      content_version TEXT NOT NULL,
      is_active INTEGER NOT NULL DEFAULT 1
    )''',
    '''CREATE TABLE questions (
      question_id TEXT PRIMARY KEY,
      paper_id TEXT REFERENCES papers (paper_id),
      paper_position INTEGER,
      subject_id TEXT NOT NULL REFERENCES subjects (subject_id),
      topic_id TEXT NOT NULL REFERENCES topics (topic_id),
      question_text_hi TEXT,
      question_text_en TEXT,
      options_json TEXT NOT NULL,
      correct_option_id TEXT NOT NULL,
      explanation_hi TEXT,
      explanation_en TEXT,
      source_reference TEXT NOT NULL,
      verification_status TEXT NOT NULL,
      sort_order INTEGER NOT NULL,
      content_version TEXT NOT NULL,
      is_active INTEGER NOT NULL DEFAULT 1
    )''',
    'CREATE INDEX idx_questions_topic ON questions (topic_id)',
    'CREATE INDEX idx_questions_paper ON questions (paper_id, paper_position)',
    '''CREATE TABLE attempts (
      attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
      kind TEXT NOT NULL CHECK (kind IN ('paper', 'topic')),
      paper_id TEXT REFERENCES papers (paper_id),
      topic_id TEXT REFERENCES topics (topic_id),
      question_ids_json TEXT NOT NULL,
      marking_scheme_json TEXT NOT NULL,
      content_version TEXT NOT NULL,
      status TEXT NOT NULL CHECK (status IN ('in_progress', 'submitted')),
      current_index INTEGER NOT NULL DEFAULT 0,
      started_at INTEGER NOT NULL,
      updated_at INTEGER NOT NULL,
      submitted_at INTEGER,
      total_questions INTEGER NOT NULL,
      score REAL,
      max_score REAL,
      correct_count INTEGER,
      incorrect_count INTEGER,
      unanswered_count INTEGER,
      CHECK ((kind = 'paper' AND paper_id IS NOT NULL) OR (kind = 'topic' AND topic_id IS NOT NULL))
    )''',
    'CREATE INDEX idx_attempts_status ON attempts (status, updated_at)',
    '''CREATE TABLE user_answers (
      answer_id INTEGER PRIMARY KEY AUTOINCREMENT,
      attempt_id INTEGER NOT NULL REFERENCES attempts (attempt_id) ON DELETE CASCADE,
      question_id TEXT NOT NULL REFERENCES questions (question_id),
      selected_option_id TEXT,
      correct_option_id TEXT,
      is_correct INTEGER,
      answered_at INTEGER,
      UNIQUE (attempt_id, question_id)
    )''',
    '''CREATE TABLE revision_items (
      revision_id INTEGER PRIMARY KEY AUTOINCREMENT,
      question_id TEXT NOT NULL UNIQUE REFERENCES questions (question_id),
      source_attempt_id INTEGER REFERENCES attempts (attempt_id),
      review_stage INTEGER NOT NULL,
      next_review_at INTEGER NOT NULL,
      last_reviewed_at INTEGER,
      status TEXT NOT NULL CHECK (status IN ('active', 'mastered')),
      consecutive_correct_reviews INTEGER NOT NULL DEFAULT 0,
      created_at INTEGER NOT NULL
    )''',
    'CREATE INDEX idx_revision_due ON revision_items (status, next_review_at)',
    '''CREATE TABLE review_log (
      review_id INTEGER PRIMARY KEY AUTOINCREMENT,
      revision_id INTEGER NOT NULL REFERENCES revision_items (revision_id) ON DELETE CASCADE,
      question_id TEXT NOT NULL REFERENCES questions (question_id),
      selected_option_id TEXT,
      is_correct INTEGER NOT NULL,
      reviewed_at INTEGER NOT NULL,
      stage_before INTEGER NOT NULL,
      stage_after INTEGER NOT NULL
    )''',
  ],
  // v2
  [
    'ALTER TABLE papers ADD COLUMN distribution_cleared INTEGER NOT NULL DEFAULT 0',
  ],
  // v3: papers keep their own question list so papers can share questions;
  // questions.paper_id is only read for papers installed before this version.
  [
    'ALTER TABLE papers ADD COLUMN question_ids_json TEXT',
    'ALTER TABLE papers ADD COLUMN exam TEXT',
    'ALTER TABLE papers ADD COLUMN level TEXT',
    'ALTER TABLE subjects ADD COLUMN language TEXT',
  ],
];

int get schemaVersion => migrations.length;

/// Opens (creating or migrating) the learner database. Tests pass an FFI
/// [factory] and a temporary [path].
Future<Database> openAppDatabase({DatabaseFactory? factory, String? path}) async {
  final dbFactory = factory ?? databaseFactory;
  final dbPath = path ?? p.join(await dbFactory.getDatabasesPath(), databaseFileName);
  return dbFactory.openDatabase(
    dbPath,
    options: OpenDatabaseOptions(
      version: schemaVersion,
      onConfigure: (db) => db.execute('PRAGMA foreign_keys = ON'),
      onCreate: (db, version) => _migrate(db, 0, version),
      onUpgrade: _migrate,
    ),
  );
}

Future<void> _migrate(Database db, int from, int to) async {
  final batch = db.batch();
  for (var version = from; version < to; version++) {
    for (final sql in migrations[version]) {
      batch.execute(sql);
    }
  }
  await batch.commit(noResult: true);
}
