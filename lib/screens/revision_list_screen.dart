import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/revision.dart';
import '../widgets/async_loader.dart';
import '../widgets/common.dart';
import 'review_screen.dart';

class _RevisionLists {
  const _RevisionLists(this.active, this.mastered);

  final List<RevisionItem> active;
  final List<RevisionItem> mastered;
}

/// Every question in revision, split into due today, upcoming and mastered.
class RevisionListScreen extends StatelessWidget {
  const RevisionListScreen({super.key});

  static Future<void> open(BuildContext context) => Navigator.of(context).push(
        MaterialPageRoute<void>(builder: (_) => const RevisionListScreen()),
      );

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    return Scaffold(
      appBar: AppBar(title: Text(s.revisionList)),
      body: AsyncLoader<_RevisionLists>(
        load: (app) async =>
            _RevisionLists(await app.progress.activeRevisionItems(), await app.progress.masteredRevisionItems()),
        builder: (context, lists) {
          final now = DateTime.now();
          final due = lists.active.where((i) => i.state.isDue(now)).toList();
          final upcoming = lists.active.where((i) => !i.state.isDue(now)).toList();
          if (lists.active.isEmpty && lists.mastered.isEmpty) {
            return EmptyState(icon: Icons.replay, title: s.revisionListEmpty, message: s.revisionEmptyHint);
          }
          return ListView(
            padding: const EdgeInsets.all(16),
            children: [
              if (due.isNotEmpty) ...[
                SectionHeader('${s.dueToday} (${due.length})'),
                for (final item in due) _RevisionTile(item: item, kind: _Kind.due),
                const SizedBox(height: 8),
                FilledButton(onPressed: () => ReviewScreen.open(context), child: Text(s.reviseNow)),
              ],
              if (upcoming.isNotEmpty) ...[
                SectionHeader('${s.upcoming} (${upcoming.length})'),
                for (final item in upcoming) _RevisionTile(item: item, kind: _Kind.upcoming),
              ],
              if (lists.mastered.isNotEmpty) ...[
                SectionHeader('${s.mastered} (${lists.mastered.length})'),
                for (final item in lists.mastered) _RevisionTile(item: item, kind: _Kind.mastered),
              ],
            ],
          );
        },
      ),
    );
  }
}

enum _Kind { due, upcoming, mastered }

class _RevisionTile extends StatelessWidget {
  const _RevisionTile({required this.item, required this.kind});

  final RevisionItem item;
  final _Kind kind;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final question = app.content.question(item.questionId);
    final steps = app.progress.scheduler.reviewsToMaster;
    final subtitle = switch (kind) {
      _Kind.due => s.reviewStep(item.state.stage, steps),
      _Kind.upcoming => '${s.dueOn(formatDate(context, item.state.nextReviewAt))} · ${s.reviewStep(item.state.stage, steps)}',
      _Kind.mastered => item.state.lastReviewedAt == null ? s.mastered : formatDate(context, item.state.lastReviewedAt!),
    };
    return Card(
      child: ListTile(
        leading: Icon(switch (kind) {
          _Kind.due => Icons.notifications_active_outlined,
          _Kind.upcoming => Icons.schedule,
          _Kind.mastered => Icons.check_circle_outline,
        }),
        title: Text(
          question?.text.resolve(question.displayLanguage(app.language)).text ?? item.questionId,
          maxLines: 2,
          overflow: TextOverflow.ellipsis,
        ),
        subtitle: Text(subtitle),
      ),
    );
  }
}
