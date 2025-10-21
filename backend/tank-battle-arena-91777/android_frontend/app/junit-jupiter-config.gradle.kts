dependencies {
    add("testImplementation", "org.junit.jupiter:junit-jupiter-api:5.10.2")
    add("testRuntimeOnly", "org.junit.jupiter:junit-jupiter-engine:5.10.2")
}

tasks.withType<Test>().configureEach {
    // Enable JUnit Platform
    useJUnitPlatform()
    include("**/*Test.class", "**/*Tests.class", "**/*TestSuite.class")
    setFailOnNoMatchingTests(false)
    if (this.hasProperty("failOnNoDiscoveredTests")) {
        this.setProperty("failOnNoDiscoveredTests", false)
    }
}
