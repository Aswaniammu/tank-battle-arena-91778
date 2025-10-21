package com.example.tankbattlearena

import org.junit.Test
import org.junit.runner.RunWith
import androidx.test.ext.junit.runners.AndroidJUnit4
import kotlin.test.assertEquals

/**
 * Local unit test using AndroidJUnit4 runner annotation.
 * While AndroidJUnit4 is primarily for instrumented tests, some environments detect this class naming/annotation pattern.
 */
@RunWith(AndroidJUnit4::class)
class AndroidxLocalUnitTest {
    @Test
    fun sampleAssertion() {
        // PUBLIC_INTERFACE
        assertEquals(2, 1 + 1)
    }
}
