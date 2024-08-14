from selenium.webdriver.common.by import By

from elements import HeaderLinks
from helpers import BASE_URL
from locators.main_locators import MainLocators
from pages import BasePage


class MainPage(BasePage, MainLocators, HeaderLinks):

    def __init__(self, driver):
        super().__init__(driver)

#   @allure.step("Open page demowebshop.tricentis.com")
    def open(self):
        self.driver.get(BASE_URL)

#    @allure.step("Assert that main is opened")
    def assert_that_main_is_opened(self):
        assert self.get_element(By.CSS_SELECTOR, self.HEADER_LOGO)
        assert self.get_element(By.CSS_SELECTOR, self.HEADER_MENU)
        assert self.get_element(By.CSS_SELECTOR, self.SLIDER)

        self.save_screenshot('assert_that_main_is_opened.png')

