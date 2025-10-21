package com.example.tankbattlearena;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * Minimal test in the 'utilities' module to ensure Gradle discovers at least one test
 * across the multi-module build on CI environments.
 */
public class UtilitiesSmokeTest {

    @Test
    public void addition_isCorrect() {
        // PUBLIC_INTERFACE
        assertEquals(4, 2 + 2);
    }
}
