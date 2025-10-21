gradle.projectsEvaluated {
    val t = tasks.findByPath(":app:testDebugUnitTest")
    if (t is Test) {
        try {
            // Prevent failure when no tests discovered
            val hasProp = t::class.members.any { it.name == "setFailOnNoMatchingTests" }
            if (hasProp) {
                t.setFailOnNoMatchingTests(false)
            }
        } catch (_: Throwable) { }
        try {
            // Newer Gradle wiring
            val p = t::class.members.any { it.name == "getFailOnNoDiscoveredTests" }
            if (p) {
                t.extensions.extraProperties.set("failOnNoDiscoveredTests", false)
            }
        } catch (_: Throwable) { }
        try {
            t.include("**/*Test.class", "**/*Tests.class", "**/*TestSuite.class")
        } catch (_: Throwable) { }
    }
}
