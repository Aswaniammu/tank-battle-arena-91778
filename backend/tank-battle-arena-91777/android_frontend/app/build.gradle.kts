plugins {
    id("com.android.application")
    kotlin("android")
}

android {
    namespace = "com.example.tankbattlearena"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.example.tankbattlearena"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        debug {
            // CI-friendly test behavior
            testOptions {
                unitTests.all {
                    it.setFailOnNoTest(false)
                    it.failOnNoMatchingTests = false
                }
            }
        }
        release {
            isMinifyEnabled = false
            testOptions {
                unitTests.all {
                    it.setFailOnNoTest(false)
                    it.failOnNoMatchingTests = false
                }
            }
        }
    }

    testOptions {
        unitTests.all {
            it.setFailOnNoTest(false)
            it.failOnNoMatchingTests = false
        }
        unitTests.isIncludeAndroidResources = true
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = "17"
    }
}

dependencies {
    implementation("org.jetbrains.kotlin:kotlin-stdlib:1.9.25")

    implementation("androidx.core:core-ktx:1.13.1")
    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("com.google.android.material:material:1.12.0")

    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.ext:junit:1.2.1")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.6.1")
}

// Fallback explicit task config to be extra safe for common unit test tasks
tasks.matching { it.name == "testDebugUnitTest" || it.name == "testReleaseUnitTest" }.configureEach {
    it.setProperty("failOnNoMatchingTests", false)
    it.setProperty("failOnNoTest", false)
}
