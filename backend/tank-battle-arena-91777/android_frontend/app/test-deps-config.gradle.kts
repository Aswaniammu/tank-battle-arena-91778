dependencies {
    add("testImplementation", "junit:junit:4.13.2")
}

android {
    testOptions {
        unitTests.all {
            useJUnit()
            // Prevent CI failures when no tests are found
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
