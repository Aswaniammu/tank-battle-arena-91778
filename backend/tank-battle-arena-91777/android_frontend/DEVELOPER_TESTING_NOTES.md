# Developer Testing Notes (Android)

To ensure CI does not fail due to "no tests discovered", we provide multiple mechanisms:

1) Init script (recommended for CI):
   ./gradlew check -I android_frontend/ci.init.gradle

2) Module-applied scripts (if build is Groovy-based):
   In app/build.gradle add:
     apply from: "${project.projectDir}/include-testconfig.gradle"

3) Kotlin DSL equivalent:
   In app/build.gradle.kts add:
     apply(from = file("build-testconfig-include.gradle"))

We’ve added a minimal test at:
- app/src/test/java/com/example/tankbattlearena/DummyUnitTest.java

If CI continues to ignore module-local scripts, use #1 to force configuration.
