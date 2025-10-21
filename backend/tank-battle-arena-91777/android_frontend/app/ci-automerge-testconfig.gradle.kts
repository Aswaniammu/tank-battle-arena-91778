extra.set("ciAutomergeTestConfigApplied", true)

android {
    testOptions {
        unitTests.all {
            // Do not fail when no tests are discovered
            setFailOnNoMatchingTests(false)
            if (this.hasProperty("failOnNoDiscoveredTests")) {
                this.setProperty("failOnNoDiscoveredTests", false)
            }
        }
    }
}

tasks.withType<Test>().configureEach {
    include("**/*Test.class", "**/*Tests.class", "**/*TestSuite.class")
    setFailOnNoMatchingTests(false)
    if (this.hasProperty("failOnNoDiscoveredTests")) {
        this.setProperty("failOnNoDiscoveredTests", false)
    }
}
