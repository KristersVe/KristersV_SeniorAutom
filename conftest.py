import time
import pytest
from appium import webdriver as appium_webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from selenium import webdriver as selenium_webdriver
from appium_setup import AppiumDriverSetup
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def chrome_driver():
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
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


@pytest.fixture
def setup_appium():
    appdriver = AppiumDriverSetup()
    yield appdriver
    appdriver.quit_driver()


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

    appium_service = AppiumService()
    appium_service.start()

    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

    driver = appium_webdriver.Remote(command_executor='http://localhost:4723', options=capabilities_options)
    time.sleep(10)

    yield driver

    driver.quit()
    appium_service.stop()
