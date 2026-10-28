import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';

import 'app_state.dart';
import 'l10n/strings.dart';
import 'screens/home_screen.dart';
import 'screens/language_choice_screen.dart';
import 'screens/papers_screen.dart';
import 'screens/practice_screen.dart';
import 'screens/progress_screen.dart';

ThemeData buildTheme(Brightness brightness) {
  final scheme = ColorScheme.fromSeed(seedColor: const Color(0xFF1F6F5C), brightness: brightness);
  return ThemeData(
    colorScheme: scheme,
    appBarTheme: const AppBarTheme(centerTitle: false),
  );
}

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
          theme: buildTheme(Brightness.light),
          darkTheme: buildTheme(Brightness.dark),
          home: snapshot.hasError
              ? _StartupError(
                  error: snapshot.error!,
                  onRetry: () => setState(() => _boot = widget.boot()),
                )
              : const Scaffold(body: Center(child: CircularProgressIndicator())),
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
      theme: buildTheme(Brightness.light),
      darkTheme: buildTheme(Brightness.dark),
      locale: Locale(app.language.name),
      supportedLocales: const [Locale('hi'), Locale('en')],
      localizationsDelegates: GlobalMaterialLocalizations.delegates,
      home: app.hasChosenLanguage ? const HomeShell() : const LanguageChoiceScreen(),
    );
  }
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

/// The four main sections behind a persistent bottom navigation bar. Tabs
/// stay alive so switching keeps scroll position and loaded data.
class HomeShell extends StatefulWidget {
  const HomeShell({super.key});

  @override
  State<HomeShell> createState() => _HomeShellState();
}

class _HomeShellState extends State<HomeShell> {
  MainTab _tab = MainTab.home;

  void _goTo(MainTab tab) => setState(() => _tab = tab);

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    return Scaffold(
      body: IndexedStack(
        index: _tab.index,
        children: [
          HomeScreen(onNavigate: _goTo),
          const PapersScreen(),
          const PracticeScreen(),
          const ProgressScreen(),
        ],
      ),
      bottomNavigationBar: NavigationBar(
        selectedIndex: _tab.index,
        onDestinationSelected: (i) => _goTo(MainTab.values[i]),
        destinations: [
          NavigationDestination(icon: const Icon(Icons.home_outlined), selectedIcon: const Icon(Icons.home), label: s.navHome),
          NavigationDestination(
              icon: const Icon(Icons.description_outlined), selectedIcon: const Icon(Icons.description), label: s.navPapers),
          NavigationDestination(
              icon: const Icon(Icons.edit_note_outlined), selectedIcon: const Icon(Icons.edit_note), label: s.navPractice),
          NavigationDestination(
              icon: const Icon(Icons.insights_outlined), selectedIcon: const Icon(Icons.insights), label: s.navProgress),
        ],
      ),
    );
  }
}
