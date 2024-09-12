import time

import allure

from elements import HeaderLinks
from helpers import BASE_URL
from locators import MainLocators, LoginLinkLocators, RegisterLinkLocators
from pages import BasePage


class LoginLinkPage(LoginLinkLocators, RegisterLinkLocators, HeaderLinks, MainLocators, BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(BASE_URL)

    @allure.step("Assert login page is opened")
    def assert_login_page_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_LOGIN, 'Welcome, Please Sign In!')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)

        self.save_screenshot('assert_login_page_is_opened.png')
        allure.attach.file(
            "assert_login_page_is_opened.png",
            name="assert_login_page_is_opened",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("User authorization")
    def user_authorization(self):  # Проверка логина на готовых данных
        self.fill(self.EMAIL, 'KZhuk111@mail.com')
        self.fill(self.PASSWORD, '123456Aabc')
        time.sleep(5)
        self.click_on_login_button()
        time.sleep(5)
        assert self.get_element(self.HEADER_LOGO)
        assert self.get_element(self.HEADER_MENU)
        assert self.get_element(self.SLIDER)
        assert self.get_element(self.FOOTER_MENU_WRAPPER)

        self.save_screenshot('successful_login.png')
        allure.attach.file(
            "successful_login.png",
            name="successful_login",
            attachment_type=allure.attachment_type.PNG
        )