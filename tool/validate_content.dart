// Checks a content pack before it is bundled into a release.
//
//   dart run tool/validate_content.dart [path/to/content_pack.json]
//
// Exits with code 1 when the pack has errors (the app would refuse to install it).
import 'dart:convert';
import 'dart:io';

import 'package:uptet_saathi/models/content.dart';
import 'package:uptet_saathi/services/content_validator.dart';

void main(List<String> args) {
  final path = args.isNotEmpty ? args.first : 'assets/content/content_pack.json';
  final ContentPack pack;
  try {
    pack = ContentPack.fromJson(jsonDecode(File(path).readAsStringSync()));
  } on FormatException catch (e) {
    stderr.writeln('ERROR: $path is not a valid content pack: ${e.message}');
    exit(1);
  } on FileSystemException catch (e) {
    stderr.writeln('ERROR: cannot read $path: ${e.message}');
    exit(1);
  }

  final issues = validateContentPack(pack, assetExists: (asset) => File(asset).existsSync());
  issues.forEach(stdout.writeln);

  final errors = issues.where((i) => i.isError).length;
  final verified = pack.questions.where((q) => q.verificationStatus == VerificationStatus.verified).length;
  stdout
    ..writeln()
    ..writeln('Content version : ${pack.contentVersion}')
    ..writeln('Release ready   : ${pack.releaseReady}')
    ..writeln('Subjects/topics : ${pack.subjects.length} / ${pack.topics.length}')
    ..writeln('Papers          : ${pack.papers.length}')
    ..writeln('Questions       : ${pack.questions.length} ($verified verified)')
    ..writeln('Errors/warnings : $errors / ${issues.length - errors}');
  exit(errors > 0 ? 1 : 0);
}
