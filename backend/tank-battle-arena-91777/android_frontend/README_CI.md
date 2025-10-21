# Android Frontend CI Notes

Some CI environments don't apply module-local Gradle scripts. To ensure tests don't fail due to discovery issues, run Gradle with the provided init script:

- Run unit tests:
  ./gradlew test -I android_frontend/ci.init.gradle

- Run full checks:
  ./gradlew check -I android_frontend/ci.init.gradle

This init script:
- Disables fail on no discovered tests
- Adds classic JUnit4 include patterns
- Keeps other defaults intact
