# Android CI Unit Test Discovery Notes

Some CI environments fail with:
> Task :app:testDebugUnitTest FAILED
> There are test sources present and no filters are applied, but the test task did not discover any tests to execute.

Recommended direct fix inside app/build.gradle:
android {
  testOptions {
    unitTests.all {
      it.failOnNoTests = false
      it.useJUnit()
    }
  }
}

Additionally ensure there's at least one conventional test class:
- app/src/test/java/com/tankbattlearena/DefaultDiscoveryTest.java

If modifying build.gradle is constrained, run:
./gradlew -Dtest.failOnNoTests=false testDebugUnitTest
or
org.gradle.test.failOnNoTests=false (in gradle.properties)
