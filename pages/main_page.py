import allure

from elements import HeaderLinks, HeaderMenu
from helpers import BASE_URL
from locators.main_locators import MainLocators
from pages import BasePage


class MainPage(MainLocators, HeaderLinks, HeaderMenu, BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Open page demowebshop.tricentis.com")
    def open_main_page(self):
        self.open_page(BASE_URL)

    @allure.step("Checking the opening of the main page")
    def assert_that_main_is_opened(self):
        assert self.get_element(self.HEADER_LOGO)
        assert self.get_element(self.HEADER_MENU)
        assert self.get_element(self.SLIDER)
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('main_page_is_opened.png')
