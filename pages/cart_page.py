from selenium.webdriver.common.by import By

from elements import HeaderLinks
from helpers import BASE_URL
from locators import CartLocators
from pages import BasePage


class CartPage(BasePage, CartLocators, HeaderLinks):

    def __init__(self, driver):
        super().__init__(driver)

#   @allure.step("Open page demowebshop.tricentis.com")
    def open(self):
        self.driver.get(BASE_URL)

#   @allure.step("Assert that page is opened")
    def assert_that_page_is_opened(self):
        assert self.get_element(By.CSS_SELECTOR, self.TEXT_SHOPPING_CART)
        assert self.get_element(By.CSS_SELECTOR, self.CONTINUE_SHOPPING)
        assert self.get_element(By.CSS_SELECTOR, self.TABLE)

        self.save_screenshot('assert_that_page_is_opened.png')