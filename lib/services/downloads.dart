import 'package:flutter/services.dart';

const _channel = MethodChannel('uptet_saathi/downloads');

enum SaveResult { saved, needsPermission, failed }

/// Copies a bundled asset into the phone's Downloads folder, where the
/// learner's file manager and PDF apps can find it. Android 9 and older
/// first ask for storage permission; the learner then saves again.
Future<SaveResult> saveAssetToDownloads(String asset, {required String fileName, required String mimeType}) async {
  try {
    final data = await rootBundle.load(asset);
    await _channel.invokeMethod<void>('save', {
      'name': fileName,
      'mimeType': mimeType,
      'bytes': data.buffer.asUint8List(data.offsetInBytes, data.lengthInBytes),
    });
    return SaveResult.saved;
  } on PlatformException catch (e) {
    if (e.code == 'permission') return SaveResult.needsPermission;
    return SaveResult.failed;
  } catch (_) {
    return SaveResult.failed;
  }
}
