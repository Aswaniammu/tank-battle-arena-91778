package com.tankbattlearena;

import static org.junit.Assert.assertNotNull;

import android.app.Application;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.robolectric.RobolectricTestRunner;
import org.robolectric.RuntimeEnvironment;

/**
 * Robolectric-based smoke test to ensure Android unit tests are discovered and runnable on CI.
 */
@RunWith(RobolectricTestRunner.class)
public class RobolectricSmokeTest {

    @Test
    public void applicationContext_isAvailable() {
        Application app = RuntimeEnvironment.getApplication();
        assertNotNull(app);
    }
}
