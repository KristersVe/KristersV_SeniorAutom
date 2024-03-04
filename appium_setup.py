import os
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options
from appium import webdriver as appium_webdriver


def start_appium_service():
    appium_service = AppiumService()
    appium_service.start()
    return appium_service


def stop_appium_service(appium_service):
    appium_service.stop()


def install_and_setup_app(package_path):
    os.system("adb uninstall com.ionicframework.conferenceapp")
    os.system(f"adb install {package_path}")


def create_android_driver(capabilities):
    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
    driver = appium_webdriver.Remote(command_executor='http://localhost:4723', options=capabilities_options)
    driver.implicitly_wait(10)
    return driver
