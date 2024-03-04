
from selenium.webdriver.common.by import By


class ConferenceLocators:
    SKIP_TUTORIAL_BTN = (By.XPATH, "//android.widget.Button[@text='SKIP']")
    ABOUT_TAB_BUTTON = (By.XPATH, "//android.view.View[@text='information circle About']")
    LOCATION_OPTION = (By.XPATH, "//android.widget.TextView[@text='Location']")
    SELECT_LOCATION_OK_BUTTON = (By.XPATH, "//android.widget.Button[@text='OK']")
    LOCATIONS = ["Austin, TX", "Chicago, IL", "Seattle, WA"]
    TABS = ["Schedule", "Speakers", "Map"]


class GitHubLocators:
    SIGN_IN_LINK = (By.LINK_TEXT, 'Sign in')
    LOGIN_FIELD = (By.ID, "login_field")
    PASSWORD_FIELD = (By.ID, "password")
    COMMIT_BUTTON = (By.NAME, "commit")
    REPO_DELETE_MENU_DIALOG = (By.ID, "dialog-show-repo-delete-menu-dialog")
    REPO_DELETE_CONFIRMATION_POPUP = (By.XPATH, "//dialog[@id='repo-delete-menu-dialog' and @open]")


class JitsiLocators:
    ANDROID_ROOM_INPUT = (By.XPATH, "//android.widget.EditText[@content-desc='Enter room name']")
    ANDROID_BUTTON = (By.ID, "button-text")
    FIREFOX_ROOM_INPUT = (By.ID, "enter_room_field")
    FIREFOX_BUTTON = (By.ID, "enter_room_button")
    ANDROID_NAME_INPUT = (By.XPATH, "//android.widget.EditText[@text='Enter your name']")
    ANDROID_JOIN_BUTTON = (By.ID, "button")
    FIREFOX_NAME_INPUT = (By.ID, "premeeting-name-input")
    FIREFOX_JOIN_BUTTON = (By.XPATH, "//div[@aria-label='Join meeting']")
    LOGIN_BUTTON = (By.XPATH, "//android.widget.TextView[@text='LOG-IN']")
    VIDEO_FEED_ANDROID = (By.XPATH, "//android.widget.TextView[@text=' J ']")
    VIDEO_FEED_FIREFOX = (By.XPATH, "//div[@id='dominantSpeaker' and contains(@style, 'visibility: hidden;')]")