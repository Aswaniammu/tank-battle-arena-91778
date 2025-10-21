package com.tankbattlearena

import androidx.test.core.app.ApplicationProvider
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import kotlin.test.assertNotNull

/**
 * Simple Robolectric test to ensure Android unit test discovery works in CI.
 */
@RunWith(RobolectricTestRunner::class)
class RobolectricSanityTest {

    @Test
    fun appContext_isAvailable() {
        val context = ApplicationProvider.getApplicationContext<android.content.Context>()
        assertNotNull(context)
    }
}
