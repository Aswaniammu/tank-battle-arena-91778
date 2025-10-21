# CI Wrapper Usage

Use the provided wrapper to ensure Gradle applies init scripts that prevent failures when no tests are discovered:
- Run checks:
  ./android_frontend/gradlew-ci check
- Or tests only:
  ./android_frontend/gradlew-ci test

If your CI cannot execute the wrapper, pass the init scripts directly:
./gradlew check -I android_frontend/ci.no-fail-tests.init.gradle -I android_frontend/ci.junit-platform.init.gradle -I android_frontend/ci.properties-flags.init.gradle
