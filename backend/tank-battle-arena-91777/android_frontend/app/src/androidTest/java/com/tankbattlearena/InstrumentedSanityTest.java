package com.tankbattlearena;

import android.content.Context;

import androidx.test.core.app.ApplicationProvider;
import androidx.test.ext.junit.runners.AndroidJUnit4;

import org.junit.Test;
import org.junit.runner.RunWith;

import static org.junit.Assert.assertNotNull;

/**
 * Minimal instrumented test to ensure Android test discovery.
 */
@RunWith(AndroidJUnit4.class)
public class InstrumentedSanityTest {

    @Test
    public void appContext_isAvailable() {
        Context context = ApplicationProvider.getApplicationContext();
        assertNotNull(context);
    }
}
