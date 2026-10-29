import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_localizations/flutter_localizations.dart';

import 'app_state.dart';
import 'l10n/strings.dart';
import 'screens/home_screen.dart';
import 'screens/language_choice_screen.dart';
import 'screens/papers_screen.dart';
import 'screens/practice_screen.dart';
import 'screens/progress_screen.dart';
import 'theme.dart';
import 'widgets/brand.dart';

/// Starts the app: shows a splash while [boot] runs, then the main UI, or a
/// bilingual error screen when no study content can be loaded.
class UptetSaathiApp extends StatefulWidget {
  const UptetSaathiApp({super.key, required this.boot});

  final Future<AppController> Function() boot;

  @override
  State<UptetSaathiApp> createState() => _UptetSaathiAppState();
}

class _UptetSaathiAppState extends State<UptetSaathiApp> {
  late Future<AppController> _boot = widget.boot();

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<AppController>(
      future: _boot,
      builder: (context, snapshot) {
        final controller = snapshot.data;
        if (controller != null) {
          return AppScope(controller: controller, child: const _LoadedApp());
        }
        return MaterialApp(
          debugShowCheckedModeBanner: false,
          theme: buildTheme(),
          home: snapshot.hasError
              ? _StartupError(
                  error: snapshot.error!,
                  onRetry: () => setState(() => _boot = widget.boot()),
                )
              : const _Splash(),
        );
      },
    );
  }
}

class _LoadedApp extends StatelessWidget {
  const _LoadedApp();

  @override
  Widget build(BuildContext context) {
    final app = AppScope.of(context);
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      onGenerateTitle: (context) => S.of(context).appName,
      theme: buildTheme(),
      locale: Locale(app.language.name),
      supportedLocales: const [Locale('hi'), Locale('en')],
      localizationsDelegates: GlobalMaterialLocalizations.delegates,
      home: app.hasChosenLanguage ? const HomeShell() : const LanguageChoiceScreen(),
    );
  }
}

/// Same mint and logo as the Android launch screen, so start-up looks continuous.
class _Splash extends StatelessWidget {
  const _Splash();

  @override
  Widget build(BuildContext context) => Scaffold(
        backgroundColor: AppColors.mint,
        body: Center(
          child: Padding(
            padding: const EdgeInsets.all(32),
            child: Image.asset(BrandAssets.logo, width: 320),
          ),
        ),
      );
}

class _StartupError extends StatelessWidget {
  const _StartupError({required this.error, required this.onRetry});

  final Object error;
  final VoidCallback onRetry;

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    return Scaffold(
      body: SafeArea(
        child: ListView(
          padding: const EdgeInsets.all(24),
          children: [
            Icon(Icons.error_outline, size: 48, color: theme.colorScheme.error),
            const SizedBox(height: 16),
            Text('अध्ययन सामग्री लोड नहीं हो सकी।\nStudy content could not be loaded.',
                style: theme.textTheme.titleMedium),
            const SizedBox(height: 8),
            const Text('कृपया ऐप दोबारा इंस्टॉल करें या उसे देने वाले व्यक्ति से संपर्क करें।\n'
                'Please reinstall the app or contact the person who shared it.'),
            const SizedBox(height: 16),
            FilledButton(onPressed: onRetry, child: const Text('फिर से प्रयास करें / Try again')),
            const SizedBox(height: 24),
            Text('$error', style: theme.textTheme.bodySmall),
          ],
        ),
      ),
    );
  }
}

enum MainTab { home, papers, practice, progress }

/// The four main sections behind a persistent bottom bar. Each tab keeps its
/// own page stack, so a paper or subject opens with the bar still visible.
/// Tests, results and reviews open full screen above the bar.
class HomeShell extends StatefulWidget {
  const HomeShell({super.key});

  @override
  State<HomeShell> createState() => _HomeShellState();
}

class _HomeShellState extends State<HomeShell> {
  MainTab _tab = MainTab.home;
  final _navigators = {for (final tab in MainTab.values) tab: GlobalKey<NavigatorState>()};

  /// Tapping the open tab again goes back to its first page.
  void _goTo(MainTab tab) {
    if (tab == _tab) {
      _navigators[tab]!.currentState?.popUntil((route) => route.isFirst);
    } else {
      setState(() => _tab = tab);
    }
  }

  /// Back closes the open tab's pages first, then returns to Home, then leaves the app.
  Future<void> _back() async {
    if (await _navigators[_tab]!.currentState!.maybePop()) return;
    if (_tab != MainTab.home) {
      setState(() => _tab = MainTab.home);
    } else {
      await SystemNavigator.pop();
    }
  }

  Widget _root(MainTab tab) => switch (tab) {
        MainTab.home => HomeScreen(onNavigate: _goTo),
        MainTab.papers => const PapersScreen(),
        MainTab.practice => const PracticeScreen(),
        MainTab.progress => const ProgressScreen(),
      };

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, _) {
        if (!didPop) _back();
      },
      child: Scaffold(
        body: IndexedStack(
          index: _tab.index,
          children: [
            for (final tab in MainTab.values)
              Navigator(
                key: _navigators[tab],
                onGenerateRoute: (settings) =>
                    MaterialPageRoute<void>(settings: settings, builder: (_) => _root(tab)),
              ),
          ],
        ),
        bottomNavigationBar: BrandNavBar(
          selected: _tab.index,
          onSelect: (i) => _goTo(MainTab.values[i]),
          items: [
            (icon: BrandAssets.navHome, label: s.navHome),
            (icon: BrandAssets.navPapers, label: s.navPapers),
            (icon: BrandAssets.navPractice, label: s.navPractice),
            (icon: BrandAssets.navProgress, label: s.navProgress),
          ],
        ),
      ),
    );
  }
}
