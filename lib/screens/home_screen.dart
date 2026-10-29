import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

import '../app.dart';
import '../app_state.dart';
import '../config.dart';
import '../l10n/strings.dart';
import '../models/attempt.dart';
import '../services/share_app.dart';
import '../theme.dart';
import '../widgets/async_loader.dart';
import '../widgets/brand.dart';
import '../widgets/common.dart';
import '../widgets/settings_sheet.dart';
import 'quiz_screen.dart';
import 'syllabus_screen.dart';

Future<void> _openWhatsAppGroup(BuildContext context) async {
  final s = S.of(context);
  final messenger = ScaffoldMessenger.of(context);
  var opened = false;
  try {
    opened = await launchUrl(Uri.parse(AppConfig.whatsAppGroupUrl), mode: LaunchMode.externalApplication);
  } catch (e) {
    debugPrint('Could not open WhatsApp group: $e');
  }
  if (!opened) messenger.showSnackBar(SnackBar(content: Text(s.whatsAppOpenFailed)));
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key, required this.onNavigate});

  final ValueChanged<MainTab> onNavigate;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    return Scaffold(
      body: Column(
        children: [
          const BrandHeader(),
          Expanded(
            child: AsyncLoader<_Resume>(
              load: (app) async => _Resume(await app.progress.latestInProgress()),
              builder: (context, data) => ListView(
                padding: const EdgeInsets.only(bottom: 24),
                children: [
                  Padding(
                    padding: const EdgeInsets.fromLTRB(20, 16, 16, 12),
                    child: Row(
                      children: [
                        Expanded(
                          child: Text(s.welcomeTitle,
                              style: const TextStyle(color: Colors.white, fontSize: 30, fontWeight: FontWeight.w700)),
                        ),
                        const _LanguagePill(),
                      ],
                    ),
                  ),
                  Semantics(
                    label: s.bannerDescription,
                    button: true,
                    excludeSemantics: true,
                    child: GestureDetector(
                      onTap: () => _openWhatsAppGroup(context),
                      child: Image.asset(BrandAssets.banner, width: double.infinity, fit: BoxFit.fitWidth),
                    ),
                  ),
                  Padding(
                    padding: const EdgeInsets.fromLTRB(16, 20, 16, 0),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        if (app.contentWarning != null) ...[
                          NoticeBanner(icon: Icons.warning_amber, text: s.contentUpdateFailed),
                          const SizedBox(height: 16),
                        ],
                        if (data.attempt case final attempt?) ...[
                          _ResumeCard(attempt: attempt),
                          const SizedBox(height: 8),
                        ],
                        SectionTitle(s.startStudying),
                        BrandCard(
                          icon: const Icon(Icons.description_outlined),
                          title: s.previousPapers,
                          subtitle: s.papersSubtitle,
                          onTap: () => onNavigate(MainTab.papers),
                        ),
                        BrandCard(
                          icon: const Icon(Icons.draw_outlined),
                          title: s.practiceAndRevision,
                          subtitle: s.practiceSubtitle,
                          onTap: () => onNavigate(MainTab.practice),
                        ),
                        BrandCard(
                          icon: const Icon(Icons.bar_chart),
                          title: s.syllabus,
                          subtitle: s.syllabusSubtitle,
                          onTap: () => SyllabusScreen.open(context),
                        ),
                        BrandCard(
                          icon: const Icon(Icons.share_outlined),
                          title: s.shareApp,
                          subtitle: s.shareAppSubtitle,
                          onTap: () => shareApp(context),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class _Resume {
  const _Resume(this.attempt);

  final Attempt? attempt;
}

/// Current language with a translate icon; opens the settings sheet.
class _LanguagePill extends StatelessWidget {
  const _LanguagePill();

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    final app = AppScope.of(context);
    return Material(
      color: AppColors.sage,
      borderRadius: BorderRadius.circular(4),
      child: InkWell(
        onTap: () => showSettingsSheet(context),
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              const Icon(Icons.translate, color: Colors.white, size: 24),
              const SizedBox(width: 4),
              Text(s.languageName(app.language),
                  style: const TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.w700)),
              const Icon(Icons.arrow_downward, color: Colors.white, size: 22),
            ],
          ),
        ),
      ),
    );
  }
}

class _ResumeCard extends StatelessWidget {
  const _ResumeCard({required this.attempt});

  final Attempt attempt;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(color: AppColors.mint, borderRadius: BorderRadius.circular(24)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(s.continueWhereLeft,
              style: const TextStyle(color: AppColors.accentTeal, fontSize: 14, fontWeight: FontWeight.w600)),
          const SizedBox(height: 4),
          Text(attemptTitle(context, attempt),
              style: const TextStyle(color: AppColors.deepTeal, fontSize: 18, fontWeight: FontWeight.w700)),
          Text(s.questionXofY(attempt.currentIndex + 1, attempt.totalQuestions),
              style: const TextStyle(color: AppColors.deepTeal)),
          const SizedBox(height: 12),
          FilledButton.icon(
            style: FilledButton.styleFrom(backgroundColor: AppColors.teal, foregroundColor: Colors.white),
            onPressed: () => QuizScreen.open(context, attempt.id),
            icon: const Icon(Icons.play_arrow),
            label: Text(s.resume),
          ),
        ],
      ),
    );
  }
}
