import 'package:flutter/material.dart';

/// Brand palette from the UPTET Saathi design.
class AppColors {
  const AppColors._();

  static const mint = Color(0xFFC2EBDA);
  static const teal = Color(0xFF2B8F98);
  static const sage = Color(0xFF9AB8AA);
  static const deepTeal = Color(0xFF0D4A57);
  static const accentTeal = Color(0xFF2A8C93);
  static const sheet = Color(0xFF1F747C);
  static const sun = Color(0xFFF5A623);

  /// Answer feedback on white option cards.
  static const correct = Color(0xFF1E7B34);
  static const wrong = Color(0xFFC62828);

  /// Activity heat map, from no activity to most active.
  static const heatEmpty = Color(0xFFE3E6EA);
  static const heat = [Color(0xFFA6E3AE), Color(0xFF6CCB7A), Color(0xFF34B04A), Color(0xFF1E8A35), Color(0xFF0B5E22)];
}

/// One look for light and dark system settings: white text on teal, as designed.
ThemeData buildTheme() {
  const scheme = ColorScheme(
    brightness: Brightness.dark,
    primary: AppColors.mint,
    onPrimary: AppColors.deepTeal,
    primaryContainer: AppColors.mint,
    onPrimaryContainer: AppColors.deepTeal,
    secondary: AppColors.sage,
    onSecondary: Colors.white,
    secondaryContainer: AppColors.sage,
    onSecondaryContainer: Colors.white,
    tertiary: AppColors.sun,
    onTertiary: AppColors.deepTeal,
    error: Color(0xFFFFB4AB),
    onError: Color(0xFF690005),
    errorContainer: Color(0xFFFFDAD6),
    onErrorContainer: Color(0xFF410002),
    surface: AppColors.teal,
    onSurface: Colors.white,
    onSurfaceVariant: Color(0xE6FFFFFF),
    surfaceContainerLowest: AppColors.teal,
    surfaceContainerLow: AppColors.sheet,
    surfaceContainer: AppColors.sheet,
    surfaceContainerHigh: AppColors.sheet,
    surfaceContainerHighest: AppColors.sage,
    outline: Color(0xB3FFFFFF),
    outlineVariant: Color(0x61FFFFFF),
    inverseSurface: AppColors.mint,
    onInverseSurface: AppColors.deepTeal,
    inversePrimary: AppColors.deepTeal,
  );
  final base = ThemeData(colorScheme: scheme, fontFamily: 'Poppins', useMaterial3: true);
  return base.copyWith(
    scaffoldBackgroundColor: AppColors.teal,
    appBarTheme: const AppBarTheme(
      centerTitle: false,
      backgroundColor: AppColors.teal,
      foregroundColor: Colors.white,
      surfaceTintColor: Colors.transparent,
    ),
    cardTheme: CardThemeData(
      color: AppColors.sage,
      surfaceTintColor: Colors.transparent,
      elevation: 0,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
    ),
    dialogTheme: const DialogThemeData(backgroundColor: AppColors.sheet),
    bottomSheetTheme: const BottomSheetThemeData(backgroundColor: AppColors.sheet, surfaceTintColor: Colors.transparent),
    filledButtonTheme: FilledButtonThemeData(
      style: FilledButton.styleFrom(
        textStyle: const TextStyle(fontFamily: 'Poppins', fontWeight: FontWeight.w600, fontSize: 16),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      ),
    ),
    outlinedButtonTheme: OutlinedButtonThemeData(
      style: OutlinedButton.styleFrom(
        foregroundColor: Colors.white,
        side: const BorderSide(color: Colors.white70),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      ),
    ),
    textButtonTheme: TextButtonThemeData(style: TextButton.styleFrom(foregroundColor: AppColors.mint)),
  );
}
