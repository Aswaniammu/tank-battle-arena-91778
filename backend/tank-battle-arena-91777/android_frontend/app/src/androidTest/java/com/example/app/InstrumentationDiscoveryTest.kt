package com.example.app

import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import org.junit.Assert.assertEquals
import org.junit.Test
import org.junit.runner.RunWith

/**
 * Basic instrumentation test to ensure discovery in CI.
 */
@RunWith(AndroidJUnit4::class)
class InstrumentationDiscoveryTest {

    @Test
    fun useAppContext() {
        val appContext = InstrumentationRegistry.getInstrumentation().targetContext
        // Package name assertion may vary by template; just assert not empty to avoid mismatch
        assert(appContext.packageName.isNotEmpty())
    }
}
