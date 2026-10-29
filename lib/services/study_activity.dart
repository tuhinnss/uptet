import '../config.dart';

/// Questions answered and time spent on one local calendar day.
class StudyDay {
  const StudyDay({required this.day, required this.questions, required this.seconds});

  /// Local midnight.
  final DateTime day;
  final int questions;
  final int seconds;

  /// A day counts towards a streak once a question was answered or the
  /// learner studied for a little while.
  bool get isActive => questions > 0 || seconds >= AppConfig.activeDayMinSeconds;

  /// Heat map shade: -1 for no activity, otherwise 0 (light) to 4 (darkest).
  int get level {
    if (!isActive) return -1;
    var level = 0;
    for (final threshold in AppConfig.heatMapQuestionLevels) {
      if (questions >= threshold) level++;
    }
    return level;
  }
}

/// Local midnight of [time].
DateTime dateOnly(DateTime time) => DateTime(time.year, time.month, time.day);

/// `2026-10-29`: the key study days are stored under.
String dayKey(DateTime time) =>
    '${time.year.toString().padLeft(4, '0')}-${time.month.toString().padLeft(2, '0')}-${time.day.toString().padLeft(2, '0')}';

DateTime parseDayKey(String key) {
  final parts = key.split('-').map(int.parse).toList();
  return DateTime(parts[0], parts[1], parts[2]);
}

/// Monday of the week [time] falls in.
DateTime weekStart(DateTime time) => DateTime(time.year, time.month, time.day - (time.weekday - DateTime.monday));

class Streaks {
  const Streaks({required this.current, required this.best});

  final int current;
  final int best;
}

/// The current streak counts consecutive active days up to today, or up to
/// yesterday while today has no activity yet, so the streak does not look
/// broken in the morning.
Streaks streaksOf(Iterable<StudyDay> days, DateTime today) {
  final active = {for (final d in days) if (d.isActive) dateOnly(d.day)};
  // Calendar steps instead of 24-hour durations, so a DST change cannot skip a day.
  DateTime previous(DateTime d) => DateTime(d.year, d.month, d.day - 1);

  var day = dateOnly(today);
  if (!active.contains(day)) day = previous(day);
  var current = 0;
  while (active.contains(day)) {
    current++;
    day = previous(day);
  }

  var best = 0;
  for (final start in active) {
    if (active.contains(previous(start))) continue;
    var length = 0;
    for (var d = start; active.contains(d); d = DateTime(d.year, d.month, d.day + 1)) {
      length++;
    }
    if (length > best) best = length;
  }
  return Streaks(current: current, best: best);
}

/// Time studied from Monday of this week up to [today].
Duration timeThisWeek(Iterable<StudyDay> days, DateTime today) {
  final start = weekStart(today);
  final seconds = days.where((d) => !d.day.isBefore(start)).fold(0, (sum, d) => sum + d.seconds);
  return Duration(seconds: seconds);
}
