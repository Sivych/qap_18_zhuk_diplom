import allure
from selenium.webdriver.common.by import By

from elements import HeaderLinks, HeaderMenu
from helpers import BASE_URL
from locators.main_locators import MainLocators
from pages import BasePage


class MainPage(MainLocators, HeaderLinks, HeaderMenu, BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Open page demowebshop.tricentis.com")
    def open(self):
        self.driver.get(BASE_URL)

    @allure.step("Assert that main is opened")
    def assert_that_main_is_opened(self):
        assert self.get_element(self.HEADER_LOGO)
        assert self.get_element(self.HEADER_MENU)
        assert self.get_element(self.SLIDER)
        assert self.get_element(self.FOOTER_MENU_WRAPPER)

        self.save_screenshot('assert_that_main_is_opened.png')
        allure.attach.file(
            "assert_that_main_is_opened.png",
            name="assert_that_main_is_opened",
            attachment_type=allure.attachment_type.PNG
        )

    
