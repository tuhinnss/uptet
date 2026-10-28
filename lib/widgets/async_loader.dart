import 'package:flutter/material.dart';

import '../app_state.dart';
import 'common.dart';

/// Loads data from the repositories and reloads it whenever progress changes.
/// While reloading, the previous data stays on screen to avoid flicker.
class AsyncLoader<T extends Object> extends StatefulWidget {
  const AsyncLoader({super.key, required this.load, required this.builder});

  final Future<T> Function(AppController app) load;
  final Widget Function(BuildContext context, T data) builder;

  @override
  State<AsyncLoader<T>> createState() => _AsyncLoaderState<T>();
}

class _AsyncLoaderState<T extends Object> extends State<AsyncLoader<T>> {
  Future<T>? _future;
  int? _revision;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final app = AppScope.of(context);
    if (_revision != app.dataRevision) {
      _revision = app.dataRevision;
      _future = widget.load(app);
    }
  }

  void _retry() => setState(() => _future = widget.load(AppScope.read(context)));

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<T>(
      future: _future,
      builder: (context, snapshot) {
        if (snapshot.hasError && snapshot.connectionState == ConnectionState.done) {
          debugPrint('Load failed: ${snapshot.error}');
          return LoadError(onRetry: _retry);
        }
        final data = snapshot.data;
        if (data == null) return const Center(child: CircularProgressIndicator());
        return widget.builder(context, data);
      },
    );
  }
}
