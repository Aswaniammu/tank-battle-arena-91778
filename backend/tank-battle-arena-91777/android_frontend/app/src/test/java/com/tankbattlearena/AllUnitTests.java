package com.tankbattlearena;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

/**
 * Aggregated test suite to ensure Gradle discovers at least one test class across environments.
 */
@RunWith(Suite.class)
@Suite.SuiteClasses({
        SmokeUnitTest.class
})
public class AllUnitTests {
    // No-op: suite holder
}
