import 'dart:math';

import 'package:flutter/material.dart';

import '../l10n/strings.dart';
import '../services/study_activity.dart';
import '../theme.dart';
import 'common.dart';

/// Daily activity as a grid: one column per week, Monday at the top, darker
/// for more questions answered. The month picker moves the window so it
/// ends with the chosen month.
class ActivityHeatMap extends StatefulWidget {
  const ActivityHeatMap({super.key, required this.days, required this.today});

  final List<StudyDay> days;
  final DateTime today;

  @override
  State<ActivityHeatMap> createState() => _ActivityHeatMapState();
}

class _ActivityHeatMapState extends State<ActivityHeatMap> {
  late DateTime _month = DateTime(widget.today.year, widget.today.month);

  static const _gap = 3.0;
  static const _labelWidth = 40.0;

  Map<DateTime, StudyDay> get _byDay => {for (final d in widget.days) dateOnly(d.day): d};

  /// Months from the first recorded activity (at most a year back) to now.
  List<DateTime> get _months {
    final now = DateTime(widget.today.year, widget.today.month);
    final first = widget.days.isEmpty ? now : DateTime(widget.days.first.day.year, widget.days.first.day.month);
    final earliest = DateTime(now.year, now.month - 11);
    final start = first.isBefore(earliest) ? earliest : first;
    return [for (var m = now; !m.isBefore(start); m = DateTime(m.year, m.month - 1)) m];
  }

  String _monthLabel(S s, DateTime month) =>
      month.year == widget.today.year ? s.monthShort(month.month) : '${s.monthShort(month.month)} ${month.year}';

  Future<void> _pickMonth() async {
    final s = S.of(context);
    final picked = await showModalBottomSheet<DateTime>(
      context: context,
      showDragHandle: true,
      builder: (context) => SafeArea(
        child: ListView(
          shrinkWrap: true,
          children: [
            Padding(
              padding: const EdgeInsets.fromLTRB(20, 0, 20, 8),
              child: Text(s.chooseMonth, style: Theme.of(context).textTheme.titleMedium),
            ),
            for (final month in _months)
              ListTile(
                title: Text(_monthLabel(s, month)),
                trailing: month == _month ? const Icon(Icons.check) : null,
                onTap: () => Navigator.pop(context, month),
              ),
          ],
        ),
      ),
    );
    if (picked != null) setState(() => _month = picked);
  }

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final today = dateOnly(widget.today);
    final byDay = _byDay;
    final lastOfMonth = DateTime(_month.year, _month.month + 1, 0);
    final end = lastOfMonth.isAfter(today) ? today : lastOfMonth;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Material(
          color: const Color(0xFFF0FBF7),
          shape: const StadiumBorder(side: BorderSide(color: AppColors.deepTeal, width: 1.5)),
          child: InkWell(
            customBorder: const StadiumBorder(),
            onTap: _pickMonth,
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Icon(Icons.calendar_month, color: AppColors.deepTeal, size: 26),
                  const SizedBox(width: 8),
                  Text(_monthLabel(s, _month),
                      style: const TextStyle(color: AppColors.deepTeal, fontSize: 20, fontWeight: FontWeight.w700)),
                  const Icon(Icons.arrow_drop_down, color: AppColors.deepTeal),
                ],
              ),
            ),
          ),
        ),
        const SizedBox(height: 12),
        LayoutBuilder(builder: (context, constraints) {
          final weeks = ((constraints.maxWidth - _labelWidth + _gap) / 18).floor().clamp(8, 26);
          final cell = (constraints.maxWidth - _labelWidth - _gap * (weeks - 1)) / weeks;
          final lastWeek = weekStart(end);
          final firstWeek = DateTime(lastWeek.year, lastWeek.month, lastWeek.day - 7 * (weeks - 1));
          DateTime dayAt(int week, int weekday) =>
              DateTime(firstWeek.year, firstWeek.month, firstWeek.day + week * 7 + weekday);
          int? monthStartingIn(int week) {
            for (var d = 0; d < 7; d++) {
              if (dayAt(week, d).day == 1) return dayAt(week, d).month;
            }
            return null;
          }

          // Named above the week a month starts in, and above the first week
          // unless a label follows too closely. None at the right edge, where it would not fit.
          int? monthLabel(int week) {
            if (week > weeks - 2) return null;
            if (week == 0) {
              final next = monthStartingIn(1) ?? monthStartingIn(2);
              return monthStartingIn(0) ?? (next == null ? dayAt(0, 6).month : null);
            }
            return monthStartingIn(week);
          }

          return Column(
            children: [
              // Month names above the week where each month starts.
              SizedBox(
                height: 18,
                child: Row(
                  children: [
                    const SizedBox(width: _labelWidth),
                    for (var w = 0; w < weeks; w++)
                      Container(
                        width: cell + (w < weeks - 1 ? _gap : 0),
                        alignment: Alignment.centerLeft,
                        child: switch (monthLabel(w)) {
                          final month? => OverflowBox(
                              maxWidth: 60,
                              alignment: Alignment.centerLeft,
                              child: Text(s.monthShort(month), style: const TextStyle(color: Colors.white, fontSize: 11)),
                            ),
                          null => null,
                        },
                      ),
                  ],
                ),
              ),
              for (var weekday = 0; weekday < 7; weekday++)
                Padding(
                  padding: EdgeInsets.only(bottom: weekday < 6 ? _gap : 0),
                  child: Row(
                    children: [
                      SizedBox(
                        width: _labelWidth,
                        child: Text(s.weekdayLabels[weekday],
                            style: const TextStyle(color: Colors.white, fontSize: 12, fontWeight: FontWeight.w600)),
                      ),
                      for (var w = 0; w < weeks; w++) ...[
                        _Cell(
                          size: cell,
                          day: dayAt(w, weekday),
                          activity: byDay[dayAt(w, weekday)],
                          future: dayAt(w, weekday).isAfter(today),
                          isToday: dayAt(w, weekday) == today,
                        ),
                        if (w < weeks - 1) const SizedBox(width: _gap),
                      ],
                    ],
                  ),
                ),
            ],
          );
        }),
        const SizedBox(height: 10),
        Row(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            Text(s.less, style: const TextStyle(color: Colors.white, fontSize: 12)),
            const SizedBox(width: 6),
            for (final color in [AppColors.heatEmpty, ...AppColors.heat]) ...[
              Container(
                width: 12,
                height: 12,
                decoration: BoxDecoration(color: color, borderRadius: BorderRadius.circular(3)),
              ),
              const SizedBox(width: 3),
            ],
            const SizedBox(width: 3),
            Text(s.more, style: const TextStyle(color: Colors.white, fontSize: 12)),
          ],
        ),
      ],
    );
  }
}

class _Cell extends StatelessWidget {
  const _Cell({required this.size, required this.day, required this.activity, required this.future, required this.isToday});

  final double size;
  final DateTime day;
  final StudyDay? activity;
  final bool future;
  final bool isToday;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final level = activity?.level ?? -1;
    final box = Container(
      width: size,
      height: size,
      decoration: BoxDecoration(
        color: future ? Colors.transparent : (level < 0 ? AppColors.heatEmpty : AppColors.heat[min(level, 4)]),
        borderRadius: BorderRadius.circular(size / 4),
        border: isToday ? Border.all(color: AppColors.deepTeal, width: 2) : null,
      ),
    );
    if (future) return box;
    return Tooltip(
      triggerMode: TooltipTriggerMode.tap,
      message: s.dayActivity(
        formatDate(context, day),
        activity?.questions ?? 0,
        s.studyTime(Duration(seconds: activity?.seconds ?? 0)),
      ),
      child: box,
    );
  }
}
