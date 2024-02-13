import os
import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.android import UiAutomator2Options


def reinstall_app():
    """App reinstall"""
    os.system("adb uninstall com.ionicframework.conferenceapp")
    os.system("adb install /Users/kristersveveris/Downloads/conference-app-android.apk")


class AppiumDriverSetup:
    """Class for appium driver setup"""

    def __init__(self):
        self.desired_caps = {
            'platformName': 'Android',
            'deviceName': 'R5CT40ZASMM',
            'automationName': 'UiAutomator2',
            'appPackage': 'com.ionicframework.conferenceapp',
            'disableIdLocatorAutocompletion': True,
            'app': os.path.abspath('/Users/kristersveveris/Downloads/conference-app-android.apk'),
        }

        self.appium_service = AppiumService()
        self.appium_service.start()

        reinstall_app()

        self.capabilities_options = UiAutomator2Options().load_capabilities(self.desired_caps)
        self.driver = webdriver.Remote(command_executor='http://localhost:4723', options=self.capabilities_options)

        time.sleep(10)

    def quit_driver(self):
        """Quit driver"""
        self.driver.quit()
        self.appium_service.stop()
