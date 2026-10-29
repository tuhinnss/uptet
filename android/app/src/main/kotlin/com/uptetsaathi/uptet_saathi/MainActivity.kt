package com.uptetsaathi.uptet_saathi

import android.Manifest
import android.content.ContentValues
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build
import android.os.Environment
import android.provider.MediaStore
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel
import java.io.File
import java.io.IOException

class MainActivity : FlutterActivity() {
    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, "uptet_saathi/share")
            .setMethodCallHandler { call, result ->
                if (call.method != "shareText") {
                    result.notImplemented()
                    return@setMethodCallHandler
                }
                val send = Intent(Intent.ACTION_SEND).apply {
                    type = "text/plain"
                    putExtra(Intent.EXTRA_TEXT, call.argument<String>("text"))
                }
                startActivity(Intent.createChooser(send, call.argument<String>("title")))
                result.success(null)
            }
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, "uptet_saathi/downloads")
            .setMethodCallHandler { call, result ->
                if (call.method != "save") {
                    result.notImplemented()
                    return@setMethodCallHandler
                }
                val name = call.argument<String>("name")!!
                val mimeType = call.argument<String>("mimeType")!!
                val bytes = call.argument<ByteArray>("bytes")!!
                try {
                    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                        saveWithMediaStore(name, mimeType, bytes)
                    } else if (!hasStoragePermission()) {
                        requestPermissions(arrayOf(Manifest.permission.WRITE_EXTERNAL_STORAGE), 1)
                        result.error("permission", "Storage permission is needed", null)
                        return@setMethodCallHandler
                    } else {
                        @Suppress("DEPRECATION")
                        val dir = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS)
                        dir.mkdirs()
                        File(dir, name).writeBytes(bytes)
                    }
                    result.success(null)
                } catch (e: Exception) {
                    result.error("failed", e.message, null)
                }
            }
    }

    // Android 10 and newer: no permission needed to add a file to Downloads.
    private fun saveWithMediaStore(name: String, mimeType: String, bytes: ByteArray) {
        val values = ContentValues().apply {
            put(MediaStore.MediaColumns.DISPLAY_NAME, name)
            put(MediaStore.MediaColumns.MIME_TYPE, mimeType)
            put(MediaStore.MediaColumns.RELATIVE_PATH, Environment.DIRECTORY_DOWNLOADS)
            put(MediaStore.MediaColumns.IS_PENDING, 1)
        }
        val uri = contentResolver.insert(MediaStore.Downloads.EXTERNAL_CONTENT_URI, values)
            ?: throw IOException("Could not create $name")
        contentResolver.openOutputStream(uri)?.use { it.write(bytes) } ?: throw IOException("Could not write $name")
        values.clear()
        values.put(MediaStore.MediaColumns.IS_PENDING, 0)
        contentResolver.update(uri, values, null, null)
    }

    private fun hasStoragePermission() = Build.VERSION.SDK_INT < Build.VERSION_CODES.M ||
        checkSelfPermission(Manifest.permission.WRITE_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED
}
