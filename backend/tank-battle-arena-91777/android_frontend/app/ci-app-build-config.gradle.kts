plugins.withId("com.android.application") {
    extensions.configure<com.android.build.gradle.AppExtension>("android") {
        testOptions.apply {
            unitTests.isIncludeAndroidResources = true
            unitTests.all {
                it as org.gradle.api.tasks.testing.Test
                try {
                    it.setFailOnNoMatchingTests(false)
                } catch (_: Throwable) { }
                try {
                    it.useJUnit()
                } catch (_: Throwable) { }
                try {
                    it.include("**/*Test.class", "**/*Tests.class", "**/*Spec.class", "**/*TestSuite.class")
                } catch (_: Throwable) { }
            }
        }
    }
    // Add junit dependency if available via the dependency handler; safe in most setups
    try {
        dependencies.add("testImplementation", "junit:junit:4.13.2")
    } catch (_: Throwable) { }
}
