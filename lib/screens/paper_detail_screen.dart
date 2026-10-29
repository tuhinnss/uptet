import 'package:flutter/material.dart';
import 'package:pdfx/pdfx.dart';

import '../app_state.dart';
import '../l10n/strings.dart';
import '../models/attempt.dart';
import '../models/content.dart';
import '../services/downloads.dart';
import '../theme.dart';
import '../widgets/async_loader.dart';
import '../widgets/brand.dart';
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

/// A paper: start or resume it, save or read the original booklet, and see past attempts.
class PaperDetailScreen extends StatelessWidget {
  const PaperDetailScreen({super.key, required this.paperId});

  final String paperId;

  static Future<void> open(BuildContext context, String paperId) =>
      Navigator.of(context).push(MaterialPageRoute<void>(builder: (_) => PaperDetailScreen(paperId: paperId)));

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    final paper = app.content.paper(paperId);
    if (paper == null) {
      return BrandPage(children: [EmptyState(icon: Icons.error_outline, title: s.testUnavailable)]);
    }
    final questions = app.content.questionsForPaper(paperId);
    final languages = app.content.paperLanguages(paperId);
    final title = paper.exam != null && paper.level != null
        ? '${s.examName(paper.exam!)} ${paper.year ?? ''} (${s.levelWord(paper.level!)})'
        : paper.title.resolve(app.language).text;

    return Scaffold(
      body: Column(
        children: [
          const BrandHeader(showExams: false),
          Expanded(
            child: AsyncLoader<_PaperData>(
              load: (app) async => _PaperData(
                await app.progress.inProgressFor(paperId: paperId),
                await app.progress.submittedAttempts(paperId: paperId),
              ),
              builder: (context, data) => ListView(
                padding: const EdgeInsets.fromLTRB(16, 20, 16, 24),
                children: [
                  SectionTitle(title, back: true),
                  Text(paper.title.resolve(app.language).text,
                      style: const TextStyle(color: Colors.white, fontSize: 15, height: 1.4)),
                  const SizedBox(height: 10),
                  Wrap(
                    spacing: 6,
                    runSpacing: 6,
                    children: [
                      PaperBadge(paper: paper),
                      InfoChip(icon: Icons.quiz_outlined, label: s.questionsCount(questions.length)),
                      if (paper.durationMinutes != null)
                        InfoChip(icon: Icons.timer_outlined, label: s.minutes(paper.durationMinutes!)),
                      if (languages.isNotEmpty)
                        InfoChip(icon: Icons.translate, label: languages.map(s.languageName).join(' · ')),
                      InfoChip(icon: Icons.rule, label: s.marking(paper.marking)),
                    ],
                  ),
                  const SizedBox(height: 20),
                  if (questions.isEmpty)
                    Text(s.noQuestionsAvailable, style: const TextStyle(color: Colors.white))
                  else if (data.unfinished case final unfinished?) ...[
                    _ActionButton(
                      icon: Icons.play_arrow,
                      label: '${s.resume} · ${s.questionXofY(unfinished.currentIndex + 1, unfinished.totalQuestions)}',
                      onPressed: () => QuizScreen.open(context, unfinished.id),
                    ),
                    TextButton(onPressed: () => _confirmRestart(context, unfinished), child: Text(s.startAgain)),
                  ] else
                    _ActionButton(icon: Icons.play_arrow, label: s.startTest, onPressed: () => startPaper(context, paper)),
                  if (app.pdfFor(paper) case final pdf?) ...[
                    const SizedBox(height: 16),
                    _DownloadButton(paper: paper, asset: pdf),
                    const SizedBox(height: 16),
                    _PdfPreview(asset: pdf, title: paper.title.resolve(app.language).text),
                  ],
                  if (data.attempts.isNotEmpty) ...[
                    const SizedBox(height: 24),
                    SectionTitle(s.yourAttempts, size: 22),
                    for (final attempt in data.attempts)
                      InnerCard(
                        icon: const Icon(Icons.assignment_turned_in_outlined),
                        title: attemptScore(attempt),
                        subtitle: attemptSubtitle(context, attempt),
                        onTap: () => ResultScreen.open(context, attempt.id),
                      ),
                  ],
                ],
              ),
            ),
          ),
        ],
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

class _ActionButton extends StatelessWidget {
  const _ActionButton({required this.icon, required this.label, required this.onPressed});

  final IconData icon;
  final String label;
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) => FilledButton.icon(
        style: FilledButton.styleFrom(
          minimumSize: const Size.fromHeight(60),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
          textStyle: const TextStyle(fontFamily: 'Poppins', fontSize: 19, fontWeight: FontWeight.w700),
        ),
        onPressed: onPressed,
        icon: Icon(icon, size: 28),
        label: Text(label),
      );
}

class _DownloadButton extends StatefulWidget {
  const _DownloadButton({required this.paper, required this.asset});

  final Paper paper;
  final String asset;

  @override
  State<_DownloadButton> createState() => _DownloadButtonState();
}

class _DownloadButtonState extends State<_DownloadButton> {
  bool _saving = false;

  Future<void> _save() async {
    final s = S.of(context);
    final messenger = ScaffoldMessenger.of(context);
    final fileName = widget.asset.split('/').last;
    setState(() => _saving = true);
    final result = await saveAssetToDownloads(widget.asset, fileName: fileName, mimeType: 'application/pdf');
    if (!mounted) return;
    setState(() => _saving = false);
    messenger.showSnackBar(SnackBar(
      content: Text(switch (result) {
        SaveResult.saved => s.savedToDownloads(fileName),
        SaveResult.needsPermission => s.storagePermissionNeeded,
        SaveResult.failed => s.downloadFailed,
      }),
    ));
  }

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    return Material(
      color: AppColors.sage,
      borderRadius: BorderRadius.circular(24),
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: _saving ? null : _save,
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 18),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Flexible(
                child: Text(s.downloadPaper,
                    style: const TextStyle(color: Colors.white, fontSize: 24, fontWeight: FontWeight.w700)),
              ),
              const SizedBox(width: 14),
              _saving
                  ? const SizedBox(
                      width: 32, height: 32, child: CircularProgressIndicator(color: Colors.white, strokeWidth: 3))
                  : const Icon(Icons.download, color: Colors.white, size: 40),
            ],
          ),
        ),
      ),
    );
  }
}

/// The booklet inline, framed as in the design; pinch to zoom, or open it full screen.
class _PdfPreview extends StatefulWidget {
  const _PdfPreview({required this.asset, required this.title});

  final String asset;
  final String title;

  @override
  State<_PdfPreview> createState() => _PdfPreviewState();
}

class _PdfPreviewState extends State<_PdfPreview> {
  late final PdfControllerPinch _controller = PdfControllerPinch(document: PdfDocument.openAsset(widget.asset));

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Container(
          height: 520,
          padding: const EdgeInsets.all(8),
          decoration: BoxDecoration(color: const Color(0xFFA5F3F7), borderRadius: BorderRadius.circular(14)),
          child: ClipRect(
            child: PdfViewPinch(
              controller: _controller,
              backgroundDecoration: const BoxDecoration(color: Colors.white),
              builders: PdfViewPinchBuilders<DefaultBuilderOptions>(
                options: const DefaultBuilderOptions(),
                documentLoaderBuilder: (_) => const Center(child: CircularProgressIndicator(color: AppColors.teal)),
                pageLoaderBuilder: (_) => const Center(child: CircularProgressIndicator(color: AppColors.teal)),
                errorBuilder: (_, __) => Center(
                  child: Text(s.pdfFailed, style: const TextStyle(color: AppColors.deepTeal)),
                ),
              ),
            ),
          ),
        ),
        const SizedBox(height: 8),
        OutlinedButton.icon(
          onPressed: () => PdfScreen.open(context, title: widget.title, asset: widget.asset),
          icon: const Icon(Icons.fullscreen),
          label: Text(s.openFullScreen),
        ),
      ],
    );
  }
}
