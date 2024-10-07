import allure

from elements import HeaderMenu
from helpers.urls import MENU_COMPUTERS
from locators import MainLocators, MenuComputersLocators
from pages import BasePage


class MenuComputersPage(MenuComputersLocators, MainLocators, HeaderMenu, BasePage):

    def init(self, driver):
        super().__init__(driver)

    @allure.step("Open menu COMPUTERS")
    def open_menu_computers(self):
        self.open_page(MENU_COMPUTERS)

    @allure.step("Checking the opening of the menu COMPUTERS")
    def assert_that_menu_computers_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Computers')
        assert self.get_element(self.DESKTOPS_SECTION)
        assert self.get_element(self.NOTEBOOKS_SECTION)
        assert self.get_element(self.ACCESSORIES_SECTION)
        assert self.get_element(self.PAGE_BODY)
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('menu_computers_is_opened.png')

    @allure.step("Adding computer accessories to the cart through the showcase")
    def add_accessories_to_the_shopping_cart(self):
        self.click(self.TCP_COACHING_DAY_ADD_TO_CART)
        self.click(self.TCP_INSTRUCTOR_LED_TRAINING)