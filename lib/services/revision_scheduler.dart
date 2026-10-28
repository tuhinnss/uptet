import '../config.dart';
import '../models/revision.dart';

/// Rule-based revision schedule (an MVP rule, not a model of memory).
///
/// A wrong test answer schedules the first review for the next day. Each
/// correct review moves the question to the next interval; a wrong review
/// starts the sequence again. After one correct review per interval the
/// question is mastered.
class RevisionScheduler {
  const RevisionScheduler({this.intervalsDays = AppConfig.revisionIntervalsDays});

  final List<int> intervalsDays;

  int get reviewsToMaster => intervalsDays.length;

  RevisionState afterIncorrectInTest(DateTime now, {RevisionState? current}) => RevisionState(
        stage: 0,
        status: RevisionStatus.active,
        nextReviewAt: dueDay(now, intervalsDays.first),
        lastReviewedAt: current?.lastReviewedAt,
        consecutiveCorrect: 0,
      );

  RevisionState afterReview(RevisionState current, {required bool correct, required DateTime now}) {
    if (!correct) {
      return RevisionState(
        stage: 0,
        status: RevisionStatus.active,
        nextReviewAt: dueDay(now, intervalsDays.first),
        lastReviewedAt: now,
        consecutiveCorrect: 0,
      );
    }
    final stage = current.stage + 1;
    final mastered = stage >= intervalsDays.length;
    return RevisionState(
      stage: stage,
      status: mastered ? RevisionStatus.mastered : RevisionStatus.active,
      nextReviewAt: mastered ? current.nextReviewAt : dueDay(now, intervalsDays[stage]),
      lastReviewedAt: now,
      consecutiveCorrect: current.consecutiveCorrect + 1,
    );
  }
}

/// Local midnight [days] calendar days after [from]. Calendar arithmetic keeps
/// the date right across daylight-saving changes.
DateTime dueDay(DateTime from, int days) {
  final local = from.toLocal();
  return DateTime(local.year, local.month, local.day + days);
}

/// Whole calendar days from [from] to [to] in local time.
int calendarDaysBetween(DateTime from, DateTime to) {
  final a = from.toLocal(), b = to.toLocal();
  return DateTime.utc(b.year, b.month, b.day).difference(DateTime.utc(a.year, a.month, a.day)).inDays;
}
