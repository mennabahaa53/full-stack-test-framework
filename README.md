# Full-Stack Test Automation Framework

A three-layer test automation framework covering API, Web UI, and Mobile — built to practice real-world test automation patterns end-to-end, including CI/CD, containerization, and reporting.

## Overview

| Layer | Target | Tool | Tests |
|---|---|---|---|
| API | [restful-booker](https://restful-booker.herokuapp.com) | pytest + requests | 10 |
| Web UI | [automationexercise.com](https://automationexercise.com) | Selenium + Page Object Model | 5 |
| Mobile | Sauce Labs' [My Demo App](https://github.com/saucelabs/my-demo-app-android) (Android) | Appium + Page Object Model | 3 |

Each layer includes fixtures for setup/teardown, Allure reporting, and — where practical — CI/CD via GitHub Actions and Docker containerization.

## Project Structure

```
full-stack-test-framework/
├── api-tests/
│   ├── conftest.py
│   ├── test_bookings.py
│   ├── test_auth.py
│   ├── test_negative_cases.py
│   └── requirements.txt
├── web-tests/
│   ├── conftest.py
│   ├── pages/
│   │   ├── login_page.py
│   │   └── signup_page.py
│   └── tests/
│       ├── test_homepage.py
│       ├── test_login.py
│       └── test_signup.py
├── mobile-tests/
│   ├── conftest.py
│   ├── app/            # APK not included — see Mobile Setup below
│   ├── pages/
│   │   └── products_page.py
│   └── tests/
│       ├── test_app_launch.py
│       └── test_product_list.py
├── .github/workflows/
│   ├── api-tests.yml
│   └── web-tests.yml
├── Dockerfile           # API layer
├── Dockerfile.web       # Web UI layer
└── .gitignore
```

## Setup

### API Layer
```
cd api-tests
pip install -r requirements.txt
pytest
```

### Web UI Layer
```
cd web-tests
pip install pytest selenium allure-pytest
pytest
```
Runs headless by default via the shared `driver` fixture in `conftest.py`.

### Mobile Layer
Requires: Node.js, Appium (`npm install -g appium`), the UiAutomator2 driver (`appium driver install uiautomator2`), Android Studio with an emulator, and `ANDROID_HOME` set.

**The APK is not included in this repo.** Download it from [Sauce Labs' releases page](https://github.com/saucelabs/my-demo-app-android/releases) and place it at `mobile-tests/app/`.

```
cd mobile-tests
pip install pytest Appium-Python-Client
appium              # in a separate terminal, keep running
pytest
```

> Note: use whichever Python version has these packages installed if you have multiple Python versions (`py -3.13` on Windows, for example).

## Reporting

Each layer supports Allure reporting:
```
pytest --alluredir=allure-results
allure serve allure-results
```

## CI/CD

- **API layer:** fully automated via GitHub Actions (`.github/workflows/api-tests.yml`), including Docker.
- **Web UI layer:** automated via GitHub Actions (`.github/workflows/web-tests.yml`) and Dockerized (`Dockerfile.web`, using `selenium/standalone-chrome`).
  - **Known limitation:** automationexercise.com serves a bot-detection interstitial ("One moment, please…") to traffic from GitHub Actions' datacenter IPs, which causes CI runs to fail even though the suite passes locally and in Docker (run from a residential IP). This is a target-site limitation, not a defect in the test suite.
- **Mobile layer:** not automated in CI. Android emulators are resource-heavy and awkward to run reliably on GitHub-hosted runners; this was scoped out as impractical for this project rather than forced.

## Notable issues found and fixed along the way

- **Race conditions** in both Web and Mobile tests, fixed with explicit waits instead of fixed sleeps where possible.
- **Architecture mismatch** on the Android emulator: an x86_64-only system image couldn't run the ARM-built demo app; fixed by using an image with ARM translation.
- **Stale Appium sessions**: back-to-back test runs could collide on a lingering app process on the emulator, resolved with an explicit `adb uninstall` step before runs.
- **Ad-intercepted clicks** on the Web signup form, resolved with `scrollIntoView` via JavaScript execution.

## Notes

Built as a self-directed learning project to practice test automation architecture (Page Object Model, fixtures, CI/CD, containerization) across API, Web, and Mobile surfaces.
