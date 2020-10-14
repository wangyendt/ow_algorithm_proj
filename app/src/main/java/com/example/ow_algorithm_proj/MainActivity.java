package com.example.ow_algorithm_proj;

import androidx.appcompat.app.AppCompatActivity;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    private Button btnGiao;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        initView();
    }

    private void initView() {
        btnGiao = (Button) findViewById(R.id.btnGiao);
    }

    public void onBtnGiaoClick(View v) {
        if (v.getId() == R.id.btnGiao) {
            MediaPlayer mMediaPlayer = MediaPlayer.create(this, R.raw.giao);
            mMediaPlayer.start();
        }
    }
}