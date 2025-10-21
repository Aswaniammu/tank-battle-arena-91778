# Android CI Notes

To stabilize CI when unit tests are not yet implemented for the app module, the build is configured to avoid failing when Gradle does not discover tests:

- Root-level `build.gradle` sets `setFailOnNoTest(false)` and `failOnNoMatchingTests=false` for all unit test tasks.
- App-level `build.gradle` mirrors this behavior under `testOptions.unitTests.all`.
- A dummy unit test is added: `app/src/test/java/com/example/tankbattlearena/DummyTest.kt`.

If stricter behavior is desired later, remove these overrides and provide real unit tests.
