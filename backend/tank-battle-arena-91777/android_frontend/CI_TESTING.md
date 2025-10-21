# CI Testing Notes

Some CI runners do not honor module-local Gradle scripts. Use the Gradle init script to ensure test discovery does not fail:

Run Gradle with:
```bash
./gradlew test -I android_frontend/ci.init.gradle
```

or for full checks:
```bash
./gradlew check -I android_frontend/ci.init.gradle
```

What it does:
- Disables failing on no discovered tests (`failOnNoDiscoveredTests=false`)
- Disables failing on no matching tests
- Adds classic JUnit4 include patterns (`**/*Test.class`, `**/*Tests.class`, `**/*TestSuite.class`)
