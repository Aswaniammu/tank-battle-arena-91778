package com.tankbattlearena;

import org.junit.runner.JUnitCore;

/**
 * Launcher class that can be used by some CI environments to explicitly run tests via JUnitCore.
 * While Gradle normally does not need this, having a conventional entry helps discovery.
 */
public class RunAllTests {
    public static void main(String[] args) {
        JUnitCore.main(
                "com.tankbattlearena.SmokeUnitTest",
                "com.tankbattlearena.KotlinSmokeUnitTest",
                "com.tankbattlearena.ExampleUnitTest",
                "com.tankbattlearena.PlainJavaSmokeTest",
                "com.tankbattlearena.RobolectricSmokeTest",
                "com.tankbattlearena.AllUnitTests"
        );
    }
}
