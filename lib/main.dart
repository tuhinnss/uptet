import 'package:flutter/material.dart';

import 'app.dart';
import 'services/bootstrap.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(const UptetSaathiApp(boot: bootstrap));
}
