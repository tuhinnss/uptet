import 'package:flutter/widgets.dart';

import 'models/content.dart';
import 'models/content_index.dart';
import 'repositories/progress_repository.dart';
import 'repositories/settings_repository.dart';

/// App-wide state: installed content, repositories, language, and a revision
/// counter that screens watch to reload after progress changes.
class AppController extends ChangeNotifier {
  AppController({
    required this.content,
    required this.progress,
    required SettingsRepository settings,
    required AppLanguage? language,
    this.contentWarning,
  })  : _settings = settings,
        _language = language;

  final ContentIndex content;
  final ProgressRepository progress;
  final SettingsRepository _settings;

  SettingsRepository get settings => _settings;

  /// Set when a new content pack could not be installed and the previous one is in use.
  final String? contentWarning;

  AppLanguage? _language;
  int _dataRevision = 0;

  bool get hasChosenLanguage => _language != null;
  AppLanguage get language => _language ?? AppLanguage.hi;
  int get dataRevision => _dataRevision;

  Future<void> setLanguage(AppLanguage language) async {
    _language = language;
    notifyListeners();
    try {
      await _settings.setLanguage(language);
    } catch (e) {
      // The choice still applies for this session; it is asked again next launch.
      debugPrint('Could not save language: $e');
    }
  }

  /// Call after attempts or revision records change.
  void progressChanged() {
    _dataRevision++;
    notifyListeners();
  }
}

class AppScope extends InheritedNotifier<AppController> {
  const AppScope({super.key, required AppController controller, required super.child})
      : super(notifier: controller);

  /// Rebuilds the caller when language or progress changes.
  static AppController of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType<AppScope>()!.notifier!;

  /// For event handlers: no rebuild dependency.
  static AppController read(BuildContext context) =>
      context.getInheritedWidgetOfExactType<AppScope>()!.notifier!;
}
