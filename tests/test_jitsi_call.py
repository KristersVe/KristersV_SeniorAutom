from pytest_bdd import scenarios, given, when, then

scenarios('../features/jitsi.feature')


@given('I open the Jitsi meet app')
def launch_app(jitsi_page):
    jitsi_page.open_jitsi_meet()


@when('I enter the room name')
def enter_room_name(jitsi_page):
    jitsi_page.enter_room_name()


@when('I enter my name and join the meeting')
def join_meeting(jitsi_page):
    jitsi_page.join_meeting()


@when('I login as moderator from mobile')
def click_on_login(jitsi_page):
    jitsi_page.click_on_login()


@then('I verify video feeds for both devices')
def verify_video_feed(jitsi_page):
    jitsi_page.verify_video_feed()
