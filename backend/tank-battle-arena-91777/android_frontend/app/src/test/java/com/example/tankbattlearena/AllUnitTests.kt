package com.example.tankbattlearena

import org.junit.runner.RunWith
import org.junit.runners.Suite

@RunWith(Suite::class)
@Suite.SuiteClasses(
    ExampleUnitTest::class,
    AnotherUnitTest::class,
    JavaUnitTest::class
)
class AllUnitTests
