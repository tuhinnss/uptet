import 'package:flutter/material.dart';

import '../l10n/strings.dart';
import '../services/share_app.dart';
import '../theme.dart';
import '../widgets/brand.dart';

/// Who makes UPTET Saathi and why, on the mint page from the design.
class AboutScreen extends StatelessWidget {
  const AboutScreen({super.key});

  static Future<void> open(BuildContext context) => Navigator.of(context, rootNavigator: true)
      .push(MaterialPageRoute<void>(builder: (_) => const AboutScreen()));

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    const body = TextStyle(color: Colors.black, fontSize: 17, height: 1.5);
    return Scaffold(
      backgroundColor: AppColors.mint,
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.fromLTRB(16, 8, 16, 32),
          children: [
            Row(
              children: [
                IconButton(
                  tooltip: MaterialLocalizations.of(context).backButtonTooltip,
                  icon: const Icon(Icons.arrow_back, color: AppColors.deepTeal),
                  onPressed: () => Navigator.of(context).maybePop(),
                ),
                const Spacer(),
                Image.asset(BrandAssets.logo, height: 80, semanticLabel: s.appName),
              ],
            ),
            const SizedBox(height: 8),
            SectionTitle(s.aboutUs, color: AppColors.accentTeal, size: 30),
            ClipRRect(
              borderRadius: BorderRadius.circular(4),
              child: Image.asset(BrandAssets.team, fit: BoxFit.cover, semanticLabel: s.teamPhoto),
            ),
            const SizedBox(height: 16),
            Text(s.aboutBody, style: body),
            const SizedBox(height: 20),
            const Text(S.aboutTagline, style: body),
            const SizedBox(height: 20),
            // Play's policy for apps with government information: say it is not an official app, and name the sources.
            Text(s.disclaimerTitle,
                style: const TextStyle(color: AppColors.deepTeal, fontSize: 18, fontWeight: FontWeight.w700)),
            const SizedBox(height: 4),
            Text(s.disclaimer, style: body.copyWith(fontSize: 15)),
            const SizedBox(height: 24),
            FilledButton.icon(
              style: FilledButton.styleFrom(
                backgroundColor: AppColors.teal,
                foregroundColor: Colors.white,
                minimumSize: const Size.fromHeight(54),
              ),
              onPressed: () => shareApp(context),
              icon: const Icon(Icons.share),
              label: Text(s.shareApp),
            ),
          ],
        ),
      ),
    );
  }
}
