import 'package:flutter/material.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/attempt.dart';
import '../widgets/async_loader.dart';
import '../widgets/common.dart';
import 'papers_screen.dart';
import 'pdf_screen.dart';
import 'quiz_launcher.dart';
import 'quiz_screen.dart';
import 'result_screen.dart';

class _PaperData {
  const _PaperData(this.unfinished, this.attempts);

  final Attempt? unfinished;
  final List<Attempt> attempts;
}

class PaperDetailScreen extends StatelessWidget {
  const PaperDetailScreen({super.key, required this.paperId});

  final String paperId;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final theme = Theme.of(context);
    final paper = app.content.paper(paperId);
    if (paper == null) {
      return Scaffold(appBar: AppBar(), body: EmptyState(icon: Icons.error_outline, title: s.testUnavailable));
    }
    final questions = app.content.questionsForPaper(paperId);
    final languages = app.content.paperLanguages(paperId);

    return Scaffold(
      appBar: AppBar(title: Text(s.previousPapers)),
      body: AsyncLoader<_PaperData>(
        load: (app) async => _PaperData(
          await app.progress.inProgressFor(paperId: paperId),
          await app.progress.submittedAttempts(paperId: paperId),
        ),
        builder: (context, data) {
          final unfinished = data.unfinished;
          return Column(
            children: [
              Expanded(
                child: ListView(
                  padding: const EdgeInsets.all(16),
                  children: [
                    Text(paper.title.resolve(app.language).text, style: theme.textTheme.headlineSmall),
                    const SizedBox(height: 8),
                    Align(alignment: Alignment.centerLeft, child: PaperBadge(paper: paper)),
                    const SizedBox(height: 16),
                    if (paper.year != null) _InfoRow(s.yearLabel, '${paper.year}'),
                    if (paper.paperCode != null) _InfoRow(s.paperCodeLabel, paper.paperCode!),
                    _InfoRow(s.questionsLabel, '${questions.length}'),
                    if (paper.durationMinutes != null) _InfoRow(s.durationLabel, s.minutes(paper.durationMinutes!)),
                    if (languages.isNotEmpty) _InfoRow(s.languagesLabel, languages.map(s.languageName).join(', ')),
                    _InfoRow(s.markingLabel, s.marking(paper.marking)),
                    _InfoRow(s.sourceLabel, paper.source),
                    if (paper.pdfAsset case final pdf?) ...[
                      const SizedBox(height: 8),
                      OutlinedButton.icon(
                        icon: const Icon(Icons.picture_as_pdf_outlined),
                        label: Text(s.viewPdf),
                        onPressed: () => PdfScreen.open(
                          context,
                          title: paper.title.resolve(app.language).text,
                          asset: pdf,
                        ),
                      ),
                    ] else
                      _InfoRow('PDF', s.noPdf),
                    if (data.attempts.isNotEmpty) ...[
                      SectionHeader(s.yourAttempts),
                      for (final attempt in data.attempts)
                        Card(
                          child: ListTile(
                            title: Text(attemptScore(attempt)),
                            subtitle: Text(attemptSubtitle(context, attempt)),
                            trailing: const Icon(Icons.chevron_right),
                            onTap: () => ResultScreen.open(context, attempt.id),
                          ),
                        ),
                    ],
                  ],
                ),
              ),
              SafeArea(
                top: false,
                child: Padding(
                  padding: const EdgeInsets.fromLTRB(16, 8, 16, 16),
                  child: questions.isEmpty
                      ? Text(s.noQuestionsAvailable, textAlign: TextAlign.center)
                      : unfinished == null
                          ? FilledButton.icon(
                              style: FilledButton.styleFrom(minimumSize: const Size.fromHeight(52)),
                              icon: const Icon(Icons.play_arrow),
                              label: Text(s.startTest),
                              onPressed: () => startPaper(context, paper),
                            )
                          : Column(
                              crossAxisAlignment: CrossAxisAlignment.stretch,
                              children: [
                                FilledButton.icon(
                                  style: FilledButton.styleFrom(minimumSize: const Size.fromHeight(52)),
                                  icon: const Icon(Icons.play_arrow),
                                  label: Text('${s.resume} · ${s.questionXofY(unfinished.currentIndex + 1, unfinished.totalQuestions)}'),
                                  onPressed: () => QuizScreen.open(context, unfinished.id),
                                ),
                                TextButton(
                                  onPressed: () => _confirmRestart(context, unfinished),
                                  child: Text(s.startAgain),
                                ),
                              ],
                            ),
                ),
              ),
            ],
          );
        },
      ),
    );
  }

  Future<void> _confirmRestart(BuildContext context, Attempt unfinished) async {
    final s = S.of(context);
    final app = AppScope.read(context);
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: Text(s.startAgainTitle),
        content: Text(s.startAgainBody),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context, false), child: Text(s.cancel)),
          FilledButton(onPressed: () => Navigator.pop(context, true), child: Text(s.startAgain)),
        ],
      ),
    );
    if (confirmed != true || !context.mounted) return;
    await startPaper(context, app.content.paper(paperId)!, replacing: unfinished.id);
  }
}

class _InfoRow extends StatelessWidget {
  const _InfoRow(this.label, this.value);

  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(width: 120, child: Text(label, style: theme.textTheme.bodyMedium?.copyWith(color: theme.colorScheme.outline))),
          Expanded(child: Text(value, style: theme.textTheme.bodyMedium)),
        ],
      ),
    );
  }
}
