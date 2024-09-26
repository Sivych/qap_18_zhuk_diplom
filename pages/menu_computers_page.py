import allure

from elements import HeaderMenu
from helpers import BASE_URL
from locators import MainLocators, MenuComputersLocators
from pages import BasePage


class MenuComputersPage(MenuComputersLocators, MainLocators, HeaderMenu, BasePage):

    def init(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(BASE_URL)

    @allure.step("Assert that menu computers is opened")
    def assert_that_menu_computers_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Computers')
        assert self.get_element(self.PAGE_BODY)

    @allure.step("Add computers accessories to the shopping cart via the showcase")
    def add_accessories_to_the_shopping_cart(self):
        self.click(self.TCP_COACHING_DAY_ADD_TO_CART)
        self.click(self.TCP_INSTRUCTOR_LED_TRAINING)