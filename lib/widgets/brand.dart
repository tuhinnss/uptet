import 'package:flutter/material.dart';

import '../l10n/strings.dart';
import '../screens/about_screen.dart';
import '../theme.dart';

class BrandAssets {
  const BrandAssets._();

  static const logo = 'assets/images/logo.png';
  static const banner = 'assets/images/home_banner.png';
  static const aboutUs = 'assets/images/about_us.png';
  static const team = 'assets/images/team.jpg';
  static const navHome = 'assets/images/icons/home.png';
  static const navPapers = 'assets/images/icons/papers.png';
  static const navPractice = 'assets/images/icons/practice.png';
  static const navProgress = 'assets/images/icons/progress.png';
  static const revision = 'assets/images/icons/revision.png';
  static const syllabus = 'assets/images/icons/syllabus.png';
}

/// A main page: the mint brand header above a teal, scrollable body.
class BrandPage extends StatelessWidget {
  const BrandPage({super.key, required this.children, this.showAbout = true});

  final List<Widget> children;
  final bool showAbout;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          BrandHeader(showAbout: showAbout),
          Expanded(
            child: ListView(padding: const EdgeInsets.fromLTRB(16, 20, 16, 24), children: children),
          ),
        ],
      ),
    );
  }
}

/// Logo on the left and the About Us link on the right, on a mint band with a curved lower edge.
class BrandHeader extends StatelessWidget {
  const BrandHeader({super.key, this.showAbout = true});

  final bool showAbout;

  @override
  Widget build(BuildContext context) {
    final s = S.of(context);
    return Container(
      decoration: const BoxDecoration(
        color: AppColors.mint,
        borderRadius: BorderRadius.vertical(bottom: Radius.circular(36)),
      ),
      child: SafeArea(
        bottom: false,
        child: Padding(
          padding: const EdgeInsets.fromLTRB(8, 4, 12, 6),
          child: Row(
            children: [
              Semantics(
                label: s.appName,
                image: true,
                child: Image.asset(BrandAssets.logo, height: 72, fit: BoxFit.contain),
              ),
              const Spacer(),
              if (showAbout)
                InkWell(
                  borderRadius: BorderRadius.circular(12),
                  onTap: () => AboutScreen.open(context),
                  child: Padding(
                    padding: const EdgeInsets.all(4),
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Image.asset(BrandAssets.aboutUs, height: 44, excludeFromSemantics: true),
                        Text(
                          s.aboutUs,
                          style: const TextStyle(color: AppColors.accentTeal, fontWeight: FontWeight.w700, fontSize: 15),
                        ),
                      ],
                    ),
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}

/// Page or section title with the accent bar on its left. Shows a back
/// button when the page can be closed.
class SectionTitle extends StatelessWidget {
  const SectionTitle(this.text, {super.key, this.color = Colors.white, this.size = 26, this.back = false});

  final String text;
  final Color color;
  final double size;
  final bool back;

  @override
  Widget build(BuildContext context) {
    final canPop = back && Navigator.of(context).canPop();
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Row(
        children: [
          if (canPop)
            IconButton(
              tooltip: MaterialLocalizations.of(context).backButtonTooltip,
              icon: Icon(Icons.arrow_back, color: color),
              onPressed: () => Navigator.of(context).maybePop(),
            )
          else
            Container(width: 6, height: size + 4, margin: const EdgeInsets.only(right: 10), color: AppColors.sage),
          Expanded(
            child: Text(text, style: TextStyle(color: color, fontSize: size, fontWeight: FontWeight.w700, height: 1.2)),
          ),
        ],
      ),
    );
  }
}

/// Sage card with a white icon, title, subtitle and arrow: the main
/// navigation element of every page.
class BrandCard extends StatelessWidget {
  const BrandCard({
    super.key,
    required this.icon,
    required this.title,
    this.subtitle,
    this.onTap,
    this.trailing = Icons.arrow_forward,
  });

  final Widget icon;
  final String title;
  final String? subtitle;
  final VoidCallback? onTap;
  final IconData trailing;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: Material(
        color: AppColors.sage,
        borderRadius: BorderRadius.circular(24),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: onTap,
          child: Padding(
            padding: const EdgeInsets.fromLTRB(16, 16, 12, 16),
            child: _CardRow(icon: icon, title: title, subtitle: subtitle, trailing: trailing),
          ),
        ),
      ),
    );
  }
}

class _CardRow extends StatelessWidget {
  const _CardRow({required this.icon, required this.title, required this.subtitle, required this.trailing});

  final Widget icon;
  final String title;
  final String? subtitle;
  final IconData trailing;

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        IconTheme(data: const IconThemeData(color: Colors.white, size: 52), child: icon),
        const SizedBox(width: 14),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(title,
                  style: const TextStyle(color: Colors.white, fontSize: 21, fontWeight: FontWeight.w700, height: 1.2)),
              if (subtitle != null)
                Text(subtitle!, style: const TextStyle(color: Colors.white, fontSize: 15, height: 1.3)),
            ],
          ),
        ),
        Icon(trailing, color: Colors.white, size: 44),
      ],
    );
  }
}

/// A [BrandCard] that opens in place to show [children], the inner mint cards.
class ExpandableBrandCard extends StatefulWidget {
  const ExpandableBrandCard({
    super.key,
    required this.icon,
    required this.title,
    this.subtitle,
    required this.children,
    this.initiallyExpanded = false,
  });

  final Widget icon;
  final String title;
  final String? subtitle;
  final List<Widget> children;
  final bool initiallyExpanded;

  @override
  State<ExpandableBrandCard> createState() => _ExpandableBrandCardState();
}

class _ExpandableBrandCardState extends State<ExpandableBrandCard> {
  late bool _expanded = widget.initiallyExpanded;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: Material(
        color: AppColors.sage,
        borderRadius: BorderRadius.circular(24),
        clipBehavior: Clip.antiAlias,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            InkWell(
              onTap: () => setState(() => _expanded = !_expanded),
              child: Semantics(
                expanded: _expanded,
                child: Padding(
                  padding: const EdgeInsets.fromLTRB(16, 16, 12, 16),
                  child: _expanded
                      ? Row(children: [
                          IconTheme(data: const IconThemeData(color: Colors.white, size: 36), child: widget.icon),
                          const SizedBox(width: 12),
                          Container(width: 6, height: 30, margin: const EdgeInsets.only(right: 8), color: AppColors.accentTeal),
                          Expanded(
                            child: Text(widget.title,
                                style: const TextStyle(color: Colors.white, fontSize: 22, fontWeight: FontWeight.w700)),
                          ),
                          const Icon(Icons.keyboard_arrow_up, color: Colors.white, size: 36),
                        ])
                      : _CardRow(
                          icon: widget.icon,
                          title: widget.title,
                          subtitle: widget.subtitle,
                          trailing: Icons.arrow_downward,
                        ),
                ),
              ),
            ),
            if (_expanded)
              Padding(
                padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
                child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: widget.children),
              ),
          ],
        ),
      ),
    );
  }
}

/// Mint card inside an expanded [ExpandableBrandCard] or listed on its own.
class InnerCard extends StatelessWidget {
  const InnerCard({
    super.key,
    this.icon,
    required this.title,
    this.subtitle,
    this.onTap,
    this.enabled = true,
    this.singleLine = false,
  });

  final Widget? icon;
  final String title;
  final String? subtitle;
  final VoidCallback? onTap;
  final bool enabled;

  /// Keeps title and subtitle to one line each, so a list of cards has equal heights.
  final bool singleLine;

  @override
  Widget build(BuildContext context) {
    final color = enabled ? AppColors.accentTeal : AppColors.accentTeal.withValues(alpha: 0.5);
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Material(
        color: AppColors.mint,
        borderRadius: BorderRadius.circular(20),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: enabled ? onTap : null,
          child: Padding(
            padding: const EdgeInsets.fromLTRB(14, 14, 10, 14),
            child: Row(
              children: [
                if (icon != null) ...[
                  IconTheme(data: IconThemeData(color: color, size: 40), child: icon!),
                  const SizedBox(width: 12),
                ],
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(title,
                          maxLines: singleLine ? 1 : null,
                          overflow: singleLine ? TextOverflow.ellipsis : null,
                          style: TextStyle(color: color, fontSize: 19, fontWeight: FontWeight.w700, height: 1.25)),
                      if (subtitle != null)
                        Text(subtitle!,
                            maxLines: singleLine ? 1 : null,
                            overflow: singleLine ? TextOverflow.ellipsis : null,
                            style: TextStyle(color: color, fontSize: 14, height: 1.3)),
                    ],
                  ),
                ),
                Icon(Icons.arrow_forward, color: color, size: 36),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

/// Mint pill button, as used under questions.
class PillButton extends StatelessWidget {
  const PillButton({super.key, required this.label, this.onPressed});

  final String label;
  final VoidCallback? onPressed;

  @override
  Widget build(BuildContext context) {
    return FilledButton(
      style: FilledButton.styleFrom(
        backgroundColor: AppColors.mint,
        foregroundColor: Colors.black87,
        disabledBackgroundColor: AppColors.mint.withValues(alpha: 0.45),
        minimumSize: const Size.fromHeight(54),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(22)),
        textStyle: const TextStyle(fontFamily: 'Poppins', fontSize: 18, fontWeight: FontWeight.w500),
      ),
      onPressed: onPressed,
      child: Text(label, maxLines: 1, overflow: TextOverflow.ellipsis),
    );
  }
}

/// Bottom navigation with the 3D icons; the selected tab sits on a sage pill.
class BrandNavBar extends StatelessWidget {
  const BrandNavBar({super.key, required this.selected, required this.onSelect, required this.items});

  final int selected;
  final ValueChanged<int> onSelect;
  final List<({String icon, String label})> items;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(
        color: AppColors.mint,
        borderRadius: BorderRadius.vertical(top: Radius.circular(28)),
      ),
      child: SafeArea(
        top: false,
        child: Padding(
          padding: const EdgeInsets.fromLTRB(8, 8, 8, 4),
          child: Row(
            children: [
              for (var i = 0; i < items.length; i++)
                Expanded(
                  child: Semantics(
                    selected: i == selected,
                    button: true,
                    label: items[i].label,
                    excludeSemantics: true,
                    child: InkWell(
                      borderRadius: BorderRadius.circular(18),
                      onTap: () => onSelect(i),
                      child: Column(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          AnimatedContainer(
                            duration: const Duration(milliseconds: 200),
                            padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 4),
                            decoration: BoxDecoration(
                              color: i == selected ? AppColors.sage : Colors.transparent,
                              borderRadius: BorderRadius.circular(18),
                            ),
                            child: Image.asset(items[i].icon, height: 44),
                          ),
                          const SizedBox(height: 2),
                          Text(
                            items[i].label,
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                            style: const TextStyle(color: Colors.black, fontSize: 14),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}

/// Stat box on the progress page: a big value, an optional "out of" note, and a label.
class StatBox extends StatelessWidget {
  const StatBox({super.key, required this.value, required this.label, this.note});

  final String value;
  final String label;
  final String? note;

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 150,
      padding: const EdgeInsets.fromLTRB(14, 12, 12, 14),
      decoration: BoxDecoration(color: AppColors.sage, borderRadius: BorderRadius.circular(24)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              Flexible(
                child: FittedBox(
                  fit: BoxFit.scaleDown,
                  alignment: Alignment.centerLeft,
                  child: Text(value,
                      style: const TextStyle(color: Colors.white, fontSize: 52, fontWeight: FontWeight.w700, height: 1.1)),
                ),
              ),
              if (note != null) ...[
                const SizedBox(width: 8),
                Flexible(
                  child: Padding(
                    padding: const EdgeInsets.only(bottom: 8),
                    child: Text(note!, style: const TextStyle(color: Colors.white, fontSize: 15, height: 1.1)),
                  ),
                ),
              ],
            ],
          ),
          const Spacer(),
          Text(label,
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
              style: const TextStyle(color: Colors.white, fontSize: 17, height: 1.15)),
        ],
      ),
    );
  }
}
