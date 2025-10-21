gradle.beforeProject {
    if (name == "app") {
        try {
            apply(from = file("include-testconfig.gradle"))
        } catch (_: Throwable) { }
        try {
            apply(from = file("test-deps-config.gradle.kts"))
        } catch (_: Throwable) { }
        try {
            apply(from = file("junit-jupiter-config.gradle.kts"))
        } catch (_: Throwable) { }
        try {
            apply(from = file("unit-test-enforce-includes.gradle"))
        } catch (_: Throwable) { }
    }
}
