from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from skimage import io, color, metrics
from PIL import Image
from io import BytesIO
from pages.locators import ConferenceLocators
import random


class ConferencePage:
    def __init__(self, driver):
        self.driver = driver

    def launch_app(self):
        assert self.driver, "Setup failed, driver not initialized"

    def skip_tutorial(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ConferenceLocators.SKIP_TUTORIAL_BTN))
            element.click()
        except TimeoutException:
            raise AssertionError("Skip tutorial button not found or not clickable")

    def click_about_tab(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ConferenceLocators.ABOUT_TAB_BUTTON))
            element.click()
        except TimeoutException:
            raise AssertionError("About tab button not found or not clickable")

    def click_location_option(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(ConferenceLocators.LOCATION_OPTION))

            screenshot = self.driver.get_screenshot_as_png()
            screenshot_image = Image.open(BytesIO(screenshot))
            bounds = (0, 88, 1080, 695)
            cropped_image = screenshot_image.crop(bounds)
            cropped_image.save('first_banner.png')
            element.click()
        except TimeoutException:
            raise AssertionError("Location tab not found or not clickable")

    def select_location(self):
        try:
            random_location = random.choice(ConferenceLocators.LOCATIONS)
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//android.widget.RadioButton[@text='{random_location}']")))
            element_text = element.text
            element.click()
            self.driver.find_element(*ConferenceLocators.SELECT_LOCATION_OK_BUTTON).click()
        except TimeoutException:
            raise AssertionError("Location option not found or not clickable")

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//android.widget.TextView[@text='{element_text}']")))
        except TimeoutException:
            raise AssertionError("Location option text not found")

        screenshot = self.driver.get_screenshot_as_png()
        screenshot_image = Image.open(BytesIO(screenshot))
        bounds = (0, 88, 1080, 695)
        cropped_image = screenshot_image.crop(bounds)
        cropped_image.save('second_banner.png')

    def verify_banner_change(self):
        image1 = io.imread('first_banner.png')
        image2 = io.imread('second_banner.png')

        # Check if the image has an alpha channel and remove it
        if image1.shape[2] == 4:
            image1 = image1[..., :3]  # Keep only the first three channels (RGB)
        if image2.shape[2] == 4:
            image2 = image2[..., :3]

        # Convert images to grayscale if needed
        if len(image1.shape) > 2:
            image1 = color.rgb2gray(image1)
        if len(image2.shape) > 2:
            image2 = color.rgb2gray(image2)

        ssim_index = metrics.structural_similarity(image1, image2, data_range=image1.max() - image1.min())
        assert ssim_index <= 0.8, "Banners did not change"

    def switch_to_other_tab(self):
        try:
            random_tab = random.choice(ConferenceLocators.TABS)
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//android.widget.TextView[@text='{random_tab}']")))
            element.click()
        except TimeoutException:
            raise AssertionError(f"Tab is not found or not clickable")

    def go_back_to_about_tab(self):
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(EC.element_to_be_clickable(ConferenceLocators.ABOUT_TAB_BUTTON))
            element.click()
        except TimeoutException:
            raise AssertionError(f"About tab is not found or not clickable")

    def verify_banner_not_changed(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(ConferenceLocators.ABOUT_TAB_BUTTON))
            WebDriverWait(self.driver, 10).until(EC.element_to_be_selected(element))
        except TimeoutException:
            raise AssertionError("About tab is not found or selected")

        screenshot = self.driver.get_screenshot_as_png()
        screenshot_image = Image.open(BytesIO(screenshot))
        bounds = (0, 88, 1080, 695)
        cropped_image = screenshot_image.crop(bounds)
        cropped_image.save('current_banner.png')

        image1 = io.imread('current_banner.png')
        image2 = io.imread('second_banner.png')

        if image1.shape[2] == 4:
            image1 = image1[..., :3]
        if image2.shape[2] == 4:
            image2 = image2[..., :3]

        if len(image1.shape) > 2:
            image1 = color.rgb2gray(image1)
        if len(image2.shape) > 2:
            image2 = color.rgb2gray(image2)

        ssim_index = metrics.structural_similarity(image1, image2, data_range=image1.max() - image1.min())
        assert ssim_index >= 0.8, "Banners did change"
