import requests
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import GitHubLocators


class GitHubPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get('https://github.com')
        assert self.driver.current_url == 'https://github.com/', "Did not land on GitHub page"

    def click_sign_in(self):
        try:
            sign_in_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GitHubLocators.SIGN_IN_LINK))
            sign_in_link.click()
        except TimeoutException:
            raise AssertionError("Sign in button not found or clickable")

    def enter_credentials(self):
        try:
            login_field = self.driver.find_element(*GitHubLocators.LOGIN_FIELD)
            login_field.send_keys("doej5")
        except NoSuchElementException:
            raise AssertionError("Login field not found")

        try:
            password_field = self.driver.find_element(*GitHubLocators.PASSWORD_FIELD)
            password_field.send_keys("doejohn222@")
        except NoSuchElementException:
            raise AssertionError("Password field element not found")

        try:
            commit_button = self.driver.find_element(*GitHubLocators.COMMIT_BUTTON)
            commit_button.click()
        except NoSuchElementException:
            raise AssertionError("Sign in button not found")

    def create_repository(self):
        username = "doej5"
        token = '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'

        repository_name = 'test_repo'
        url = f'https://api.github.com/repos/{username}/{repository_name}'
        headers = {
            'Authorization': f'token {token}'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            pass
        elif response.status_code == 404:
            url = 'https://api.github.com/user/repos'
            payload = {
                'name': 'test_repo',
            }
            response = requests.post(url, headers=headers, json=payload)

            assert response.status_code == 201, f"Failed to create repository: {response.text}"
        else:
            assert False, f"Failed to check repository existence: {response.text}"

    def open_repository_settings(self):
        self.driver.get('https://github.com/doej5/test_repo/settings')
        assert self.driver.current_url == 'https://github.com/doej5/test_repo/settings', \
            "Did not land on repository settings"

    def delete_repository(self):
        try:
            element = self.driver.find_element(*GitHubLocators.REPO_DELETE_MENU_DIALOG)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            element.click()
        except NoSuchElementException:
            raise AssertionError("Delete repository button not found")

    def validate_confirmation_popup(self):
        try:
            self.driver.find_element(*GitHubLocators.REPO_DELETE_CONFIRMATION_POPUP)
        except NoSuchElementException:
            raise AssertionError("Confirmation popup is not present")
