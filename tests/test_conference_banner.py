from pytest_bdd import given, then, when, scenarios

scenarios('../features/conference.feature')


@given('I launch the conference app')
def launch_app(conference_page):
    conference_page.launch_app()


@when('I skip the tutorial')
def skip_tutorial(conference_page):
    conference_page.skip_tutorial()


@when('I click on the about tab')
def click_about_tab(conference_page):
    conference_page.click_about_tab()


@when('I click on the location option')
def click_location_option(conference_page):
    conference_page.click_location_option()


@when('I select any other location value')
def select_location(conference_page):
    conference_page.select_location()


@then('I should see the banner change')
def verify_banner_change(conference_page):
    conference_page.verify_banner_change()


@when('I switch to any other tab')
def switch_to_other_tab(conference_page):
    conference_page.switch_to_other_tab()


@when('I go back to the about tab')
def go_back_to_about_tab(conference_page):
    conference_page.go_back_to_about_tab()


@then('I should see that banner has not changed')
def verify_banner_not_changed(conference_page):
    conference_page.verify_banner_not_changed()
