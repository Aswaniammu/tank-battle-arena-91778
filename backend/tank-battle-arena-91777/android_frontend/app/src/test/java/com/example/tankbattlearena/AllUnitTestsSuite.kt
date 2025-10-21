package com.example.tankbattlearena

import com.example.tankbattlearena.core.SimpleTruthTest
import org.junit.runner.RunWith
import org.junit.runners.Suite

@RunWith(Suite::class)
@Suite.SuiteClasses(
    SimpleTruthTest::class,
    DummyTest::class
)
class AllUnitTestsSuite
