import 'package:flutter/material.dart';
import 'package:pdfx/pdfx.dart';

import '../l10n/strings.dart';
import '../widgets/common.dart';

/// Shows a paper's original question booklet, bundled with the app, with
/// pinch to zoom. Rendering uses Android's own PDF renderer, so it works offline.
class PdfScreen extends StatefulWidget {
  const PdfScreen({super.key, required this.title, required this.asset});

  final String title;
  final String asset;

  static Future<void> open(BuildContext context, {required String title, required String asset}) =>
      Navigator.of(context, rootNavigator: true)
          .push(MaterialPageRoute<void>(builder: (_) => PdfScreen(title: title, asset: asset)));

  @override
  State<PdfScreen> createState() => _PdfScreenState();
}

class _PdfScreenState extends State<PdfScreen> {
  late final PdfControllerPinch _controller = PdfControllerPinch(document: PdfDocument.openAsset(widget.asset));
  int? _pageCount;

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final pageCount = _pageCount;
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title, maxLines: 1, overflow: TextOverflow.ellipsis),
        actions: [
          if (pageCount != null)
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16),
              child: Center(
                child: ValueListenableBuilder<int>(
                  valueListenable: _controller.pageListenable,
                  builder: (context, page, _) => Text(s.pageXofY(page, pageCount)),
                ),
              ),
            ),
        ],
      ),
      body: PdfViewPinch(
        controller: _controller,
        onDocumentLoaded: (document) => setState(() => _pageCount = document.pagesCount),
        onDocumentError: (error) => debugPrint('Could not open ${widget.asset}: $error'),
        backgroundDecoration: BoxDecoration(color: Theme.of(context).colorScheme.surfaceContainerHighest),
        builders: PdfViewPinchBuilders<DefaultBuilderOptions>(
          options: const DefaultBuilderOptions(),
          documentLoaderBuilder: (_) => const Center(child: CircularProgressIndicator()),
          pageLoaderBuilder: (_) => const Center(child: CircularProgressIndicator()),
          errorBuilder: (_, __) => EmptyState(icon: Icons.picture_as_pdf_outlined, title: s.pdfFailed),
        ),
      ),
    );
  }
}
