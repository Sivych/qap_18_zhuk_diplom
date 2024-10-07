import allure

from elements import HeaderMenu
from helpers.urls import MENU_DIGITAL_DOWNLOADS
from locators import MainLocators
from pages import BasePage


class MenuDigitalDownloadsPage(MainLocators, HeaderMenu, BasePage):

    def init(self, driver):
        super().__init__(driver)

    @allure.step("Open menu DIGITAL DOWNLOADS")
    def open_menu_digital_downloads(self):
        self.open_page(MENU_DIGITAL_DOWNLOADS)

    @allure.step("Checking the opening of the menu DIGITAL DOWNLOADS")
    def assert_that_menu_digital_downloads_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Digital downloads')
        assert self.get_element(self.PAGE_BODY)
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('menu_digital_downloads_is_opened.png')