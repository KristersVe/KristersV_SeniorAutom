from pytest_bdd import given, then, when, scenarios
from pages.conference import ConferencePage

scenarios('../features/conference.feature')


@given('I launch the conference app')
def launch_app(setup_appium):
    page = ConferencePage(setup_appium.driver)
    page.launch_app()


@when('I skip the tutorial')
def skip_tutorial(setup_appium):
    page = ConferencePage(setup_appium.driver)
    page.skip_tutorial()


@when('I click on the about tab')
def click_about_tab(setup_appium):
    page = ConferencePage(setup_appium.driver)
    page.click_about_tab()


@when('I click on the location option')
def click_location_option(setup_appium):
    page = ConferencePage(setup_appium.driver)
    page.click_location_option()


@when('I select any other location value')
def select_location(setup_appium):
    page = ConferencePage(setup_appium.driver)
    page.select_location()


@then('I should see the banner change')
def verify_banner_change(setup_appium):
    page = ConferencePage(setup_appium.driver)
    page.verify_banner_change()


@when('I switch to any other tab')
def switch_to_other_tab(setup_appium):
    page = ConferencePage(setup_appium.driver)
    page.switch_to_other_tab()


@when('I go back to the about tab')
def go_back_to_about_tab(setup_appium):
    page = ConferencePage(setup_appium.driver)
    page.go_back_to_about_tab()


@then('I should see that banner has not changed')
def verify_banner_not_changed(setup_appium):
    page = ConferencePage(setup_appium.driver)
    page.verify_banner_not_changed()
