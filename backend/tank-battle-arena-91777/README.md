# Android Frontend Notes

This Android project includes minimal unit and instrumented tests to satisfy CI test discovery:
- Unit tests: app/src/test/java and app/src/test/kotlin contain simple JUnit tests.
- Instrumented tests: app/src/androidTest/java contains a minimal test using AndroidX runner.

If CI still reports "no tests discovered", ensure:
- Gradle task is not filtering out tests.
- failOnNoTests is set to false (configured in app/build.gradle and app/tests.gradle).
- The Gradle wrapper is using Gradle 8.7 (wrapper properties provided).
- Kotlin and JUnit test dependencies are available.

You can run tests locally:
- ./gradlew testDebugUnitTest
- ./gradlew connectedAndroidTest (requires emulator/device)
