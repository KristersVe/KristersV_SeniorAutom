import os
import pytest
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.firefox.options import Options
from pages.github import GitHubPage
from pages.jitsi import JitsiPage
from pages.conference import ConferencePage
from appium_setup import start_appium_service, stop_appium_service, install_and_setup_app, create_android_driver


@pytest.fixture
def chrome_driver():
    # Could be used for headless mode
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # driver = selenium_webdriver.Chrome(options=chrome_options)

    driver = selenium_webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    options = Options()
    options.set_preference("media.navigator.permission.disabled", True)

    driver = selenium_webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def appium_driver_conf():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'R5CT40ZASMM',
        'automationName': 'UiAutomator2',
        'appPackage': 'com.ionicframework.conferenceapp',
        'appActivity': 'MainActivity',
        'disableIdLocatorAutocompletion': True,
        'app': os.path.abspath('/Users/kristersveveris/Downloads/conference-app-android.apk')
    }

    appium_service = start_appium_service()
    install_and_setup_app(desired_caps['app'])
    driver = create_android_driver(desired_caps)

    yield driver

    driver.quit()
    stop_appium_service(appium_service)

@pytest.fixture
def appium_driver_jitsi():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'R5CT40ZASMM',
        'automationName': 'UiAutomator2',
        'appPackage': 'org.jitsi.meet',
        'appActivity': 'MainActivity',
        'autoGrantPermissions': True,
        'disableIdLocatorAutocompletion': True
    }

    appium_service = start_appium_service()
    driver = create_android_driver(desired_caps)

    yield driver

    driver.quit()
    stop_appium_service(appium_service)


@pytest.fixture
def github_page(chrome_driver):
    yield GitHubPage(chrome_driver)


@pytest.fixture
def conference_page(appium_driver_conf):
    yield ConferencePage(appium_driver_conf)


@pytest.fixture
def jitsi_page(firefox_driver, appium_driver_jitsi):
    yield JitsiPage(firefox_driver, appium_driver_jitsi)


# This hook could have been used for screenshot captures
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == "call" and rep.failed:
#         try:
#             driver = item._request.getfixturevalue('driver')
#             driver.save_screenshot("failure_screenshot.png")
#         except Exception as e:
#             print("Failed to capture screenshot:", e)
#
# def pytest_html_results_table_row(report, cells):
#     if report.failed:
#         screenshot_path = report.extra['screenshot_path']
#         cells.append(pytest_html.extras.url(screenshot_path, "Screenshot"))
