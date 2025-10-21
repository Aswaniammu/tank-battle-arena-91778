package com.example.tankbattle;

import android.content.Context;

import androidx.test.core.app.ApplicationProvider;
import androidx.test.ext.junit.runners.AndroidJUnit4;

import org.junit.Test;
import org.junit.runner.RunWith;

import static org.junit.Assert.assertEquals;

/**
 * Minimal instrumentation test to satisfy test discovery if androidTest tasks run.
 */
@RunWith(AndroidJUnit4.class)
public class ExampleInstrumentedTest {
    @Test
    public void useAppContext() {
        Context appContext = ApplicationProvider.getApplicationContext();
        // Validate package name if available or just ensure context is non-null
        assertEquals(true, appContext != null);
    }
}
