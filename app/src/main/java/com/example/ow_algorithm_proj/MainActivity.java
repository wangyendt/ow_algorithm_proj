package com.example.ow_algorithm_proj;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.media.MediaPlayer;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.util.Log;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.io.File;
import java.util.EventListener;
import java.util.TreeMap;

public class MainActivity extends AppCompatActivity {

    private Button btnGiao;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        if (isStoragePermissionGranted()) {
            initView();
        }
    }


    public boolean isStoragePermissionGranted() {
        final Context context = getApplicationContext();
        int readPermissionCheck = ContextCompat.checkSelfPermission(context,
                Manifest.permission.READ_EXTERNAL_STORAGE);
        int writePermissionCheck = ContextCompat.checkSelfPermission(context,
                Manifest.permission.WRITE_EXTERNAL_STORAGE);
        if (readPermissionCheck == PackageManager.PERMISSION_GRANTED
                && writePermissionCheck == PackageManager.PERMISSION_GRANTED) {
            return true;
        } else {
            ActivityCompat.requestPermissions(this, new String[]{
                    Manifest.permission.READ_EXTERNAL_STORAGE,
                    Manifest.permission.WRITE_EXTERNAL_STORAGE}, 1);
            return false;
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            //resume tasks needing this permission
            initView();
        }
    }

    private void initView() {
        btnGiao = (Button) findViewById(R.id.btnGiao);
        String root = Environment.getExternalStorageDirectory() + "/oppo_log";
//        String[] files = Tools.list_all_files(root, new String[]{"spi", ".log"}, new String[]{}, true);
//        Toast.makeText(getApplicationContext(),
//                files.length,
//                Toast.LENGTH_LONG).show();

//        Toast.makeText(getApplicationContext(), Environment.getExternalStorageDirectory().toString(),Toast.LENGTH_LONG).show();
    }

    public void onBtnGiaoClick(View v) {
        if (v.getId() == R.id.btnGiao) {
            MediaPlayer mMediaPlayer = MediaPlayer.create(this, R.raw.giao);
            mMediaPlayer.start();
        }
    }
}