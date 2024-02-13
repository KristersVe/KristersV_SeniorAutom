import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import JitsiLocators


class JitsiPage:
    def __init__(self, firefox_driver, appium_driver_jitsi):
        self.firefox_driver = firefox_driver
        self.appium_driver_jitsi = appium_driver_jitsi

    def open_jitsi_meet(self):
        self.firefox_driver.get('https://meet.jit.si/')
        assert self.firefox_driver.current_url == 'https://meet.jit.si/', "Did not land on Jitsi meet"

    def enter_room_name(self):
        try:
            android_room_input = self.appium_driver_jitsi.find_element(*JitsiLocators.ANDROID_ROOM_INPUT)
            android_room_input.click()
            android_room_input.send_keys("ThisIsTestRoom")
        except NoSuchElementException:
            raise AssertionError("Android room input element is not clickable or not found")

        try:
            android_button = self.appium_driver_jitsi.find_element(*JitsiLocators.ANDROID_BUTTON)
            android_button.click()
        except NoSuchElementException:
            raise AssertionError("Android enter room button is not clickable or not found")

        try:
            firefox_room_input = self.firefox_driver.find_element(*JitsiLocators.FIREFOX_ROOM_INPUT)
            firefox_room_input.click()
            firefox_room_input.send_keys("ThisIsTestRoom")
        except NoSuchElementException:
            raise AssertionError("Firefox room input element is not clickable or not found")

        try:
            firefox_button = self.firefox_driver.find_element(*JitsiLocators.FIREFOX_BUTTON)
            firefox_button.click()
        except NoSuchElementException:
            raise AssertionError("Firefox enter room button is not clickable or not found")

    def join_meeting(self):
        try:
            android_name_input = WebDriverWait(self.appium_driver_jitsi, 10).until(EC.element_to_be_clickable(JitsiLocators.ANDROID_NAME_INPUT))
            android_name_input.click()
            android_name_input.send_keys("John Doe")
        except TimeoutException:
            raise AssertionError("Android enter your name input field is not present or clickable")

        try:
            android_join_button = WebDriverWait(self.appium_driver_jitsi, 10).until(EC.element_to_be_clickable(JitsiLocators.ANDROID_JOIN_BUTTON))
            android_join_button.click()
        except TimeoutException:
            raise AssertionError("Android join meeting button not found")

        try:
            firefox_name_input = WebDriverWait(self.firefox_driver, 10).until(EC.element_to_be_clickable(JitsiLocators.FIREFOX_NAME_INPUT))
            firefox_name_input.click()
            firefox_name_input.send_keys("Janis")
        except TimeoutException:
            raise AssertionError("Firefox enter your name input field is not present or clickable")

        try:
            firefox_join_button = WebDriverWait(self.firefox_driver, 10).until(EC.element_to_be_clickable(JitsiLocators.FIREFOX_JOIN_BUTTON))
            firefox_join_button.click()
        except TimeoutException:
            raise AssertionError("Firefox join meeting button not found")

    def click_on_login(self):
        try:
            element = WebDriverWait(self.appium_driver_jitsi, 10).until(EC.element_to_be_clickable(JitsiLocators.LOGIN_BUTTON))
            element.click()
        except TimeoutException:
            raise AssertionError("Android click on LOG IN button not found or clickable")

    def verify_video_feed(self):
        try:
            WebDriverWait(self.appium_driver_jitsi, 10).until(EC.visibility_of_element_located(JitsiLocators.VIDEO_FEED_ANDROID))
            time.sleep(2)
            try:
                self.appium_driver_jitsi.find_element(*JitsiLocators.VIDEO_FEED_ANDROID)
                raise AssertionError("Firefox video feed is not present")
            except NoSuchElementException:
                pass
        except TimeoutException:
            pass

        try:
            WebDriverWait(self.firefox_driver, 10).until(EC.presence_of_element_located(JitsiLocators.VIDEO_FEED_FIREFOX))
        except TimeoutException:
            raise AssertionError("Android video feed is not present")
