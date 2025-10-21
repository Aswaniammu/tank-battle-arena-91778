package com.example.tankbattlearena;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

/**
 * Ensures at least one JUnit4 test class is discovered by Gradle.
 */
@RunWith(Suite.class)
@Suite.SuiteClasses({
        ExampleUnitTest.class
})
public class AllUnitTests {
}
