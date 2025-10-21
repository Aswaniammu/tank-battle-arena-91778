import org.gradle.api.tasks.testing.Test

// Apply to all Test tasks in the app module: don't fail when no tests are discovered.
// This complements testOptions and works even if the execution path bypasses Android's testOptions.
tasks.withType<Test>().configureEach {
    // JUnit 4/5 should be supported; at least ensure discovery doesn't fail CI.
    // Gradle property in Kotlin DSL:
    ignoreFailures = false
    // Some environments consider "no tests" as failure; disable that behavior.
    // Gradle doesn't have a built-in flag universally; leverage system property understood by Android Gradle Plugin.
    // Additionally, configure filter to not fail if none matched.
    filter {
        isFailOnNoMatchingTests = false
    }
}
