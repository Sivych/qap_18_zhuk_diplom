import allure

from elements import HeaderLinks
from helpers import BASE_URL
from locators import RegisterLinkLocators, MainLocators
from pages import BasePage


class RegisterLinkPage(RegisterLinkLocators, HeaderLinks, MainLocators, BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(BASE_URL)

#    @allure.step("Assert that page is opened")
    def assert_register_page_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_REGISTER, 'Register')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)

        self.save_screenshot('assert_register_page_is_opened.png')
        allure.attach.file(
            "assert_register_page_is_opened.png",
            name="assert_register_page_is_opened",
            attachment_type=allure.attachment_type.PNG
        )