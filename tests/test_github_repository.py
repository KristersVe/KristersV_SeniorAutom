from pytest_bdd import given, then, when, scenarios

scenarios('../features/github.feature')


@given('I open the GitHub page')
def open_github_page(github_page):
    github_page.open_page()


@when('I click on sign in')
def click_sign_in(github_page):
    github_page.click_sign_in()


@when('I enter the credentials')
def enter_credentials(github_page):
    github_page.enter_credentials()


@when('I create a repository')
def create_repository(github_page):
    github_page.create_repository()


@when('I open repository settings')
def open_repository_settings(github_page):
    github_page.open_repository_settings()


@when('I try to delete repository')
def delete_repository(github_page):
    github_page.delete_repository()


@then('I see the confirmation popup')
def validate_confirmation_popup(github_page):
    github_page.validate_confirmation_popup()
