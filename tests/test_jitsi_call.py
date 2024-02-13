from pytest_bdd import scenarios, given, when, then
from pages.jitsi import JitsiPage

scenarios('../features/jitsi.feature')


@given('I open the Jitsi meet app')
def launch_app(appium_driver_jitsi, firefox_driver):
    page = JitsiPage(firefox_driver, appium_driver_jitsi)
    page.open_jitsi_meet()


@when('I enter the room name')
def enter_room_name(appium_driver_jitsi, firefox_driver):
    page = JitsiPage(firefox_driver, appium_driver_jitsi)
    page.enter_room_name()


@when('I enter my name and join the meeting')
def join_meeting(appium_driver_jitsi, firefox_driver):
    page = JitsiPage(firefox_driver, appium_driver_jitsi)
    page.join_meeting()


@when('I login as moderator from mobile')
def click_on_login(appium_driver_jitsi):
    page = JitsiPage(None, appium_driver_jitsi)
    page.click_on_login()


@then('I verify video feeds for both devices')
def verify_video_feed(appium_driver_jitsi, firefox_driver):
    page = JitsiPage(firefox_driver, appium_driver_jitsi)
    page.verify_video_feed()
