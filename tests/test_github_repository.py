from pytest_bdd import given, then, when, scenarios
from pages.github import GitHubPage

scenarios('../features/github.feature')


@given('I open the GitHub page')
def open_github_page(chrome_driver):
    page = GitHubPage(chrome_driver)
    page.open_page()


@when('I click on sign in')
def click_sign_in(chrome_driver):
    page = GitHubPage(chrome_driver)
    page.click_sign_in()


@when('I enter the credentials')
def enter_credentials(chrome_driver):
    page = GitHubPage(chrome_driver)
    page.enter_credentials()


@when('I create a repository')
def create_repository(chrome_driver):
    page = GitHubPage(chrome_driver)
    page.create_repository()


@when('I open repository settings')
def open_repository_settings(chrome_driver):
    page = GitHubPage(chrome_driver)
    page.open_repository_settings()


@when('I try to delete repository')
def delete_repository(chrome_driver):
    page = GitHubPage(chrome_driver)
    page.delete_repository()


@then('I see the confirmation popup')
def validate_confirmation_popup(chrome_driver):
    page = GitHubPage(chrome_driver)
    page.validate_confirmation_popup()
