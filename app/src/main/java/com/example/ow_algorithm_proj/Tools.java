package com.example.ow_algorithm_proj;

import android.util.Log;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Tools {
    public static String[] list_all_files(String root, String[] keys, String[] outliers,boolean full_path) {
        String tag ="list_all_files";
        Log.d(tag,"root="+root);
        List<String> _files = new ArrayList<>();
        File fRoot = new File(root);
        Log.d(tag,"new File root: "+fRoot.getAbsolutePath()+", "+fRoot.exists()+", "+fRoot.isDirectory());
        File[] files = fRoot.listFiles();
        if (files == null){
            Log.d(tag,"shit");
        }
        for (File f : fRoot.listFiles()) {
            Log.d(tag,f.getAbsolutePath()+ ", "+f.isDirectory());
            if (f.isDirectory()) {
                _files.addAll(Arrays.asList(list_all_files(f.getAbsolutePath(), keys, outliers,full_path)));
            }
            if (f.isFile()
                    && Arrays.stream(keys).allMatch(key -> f.getPath().contains(key))
                    && Arrays.stream(outliers).noneMatch(out -> f.getPath().contains(out))
            ) {
                _files.add(full_path?f.getAbsolutePath():f.getPath());
            }
        }

        String[] ret = new String[_files.size()];
        Log.d(tag,ret.length+"");
        return _files.toArray(ret);
    }
}
