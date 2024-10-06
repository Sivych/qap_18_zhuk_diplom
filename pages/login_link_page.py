import time
import allure
from generator.generator import generated_new_user

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
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Welcome, Please Sign In!')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('assert_login_page_is_opened.png')

    @allure.step("User authorization")
    def user_authorization(self):
        """Проверка логина на готовых данных"""
        dataset_email = 'KZhuk111@mail.com'
        dataset_password = '123456Aabc'
        self.fill(self.EMAIL, dataset_email)
        self.fill(self.PASSWORD, dataset_password)
        self.click_on_login_button()
        time.sleep(1)
        assert self.get_element(self.HEADER_LOGO)
        assert self.get_element(self.HEADER_MENU)
        assert self.get_element(self.SLIDER)
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('successful_login.png')

    @allure.step("Error user authorization")
    def error_user_authorization(self):
        """Проверка логина на несуществующих данных"""
        user_info = next(generated_new_user())
        email = user_info.email
        self.fill(self.EMAIL, email)
        self.fill(self.PASSWORD, '123456Aabc')
        self.click_on_login_button()
        time.sleep(1)
        assert self.get_element(self.VALIDATION_SUMMARY_ERRORS)
        self.save_screenshot('error_user_authorization.png')

    @allure.step("Assert account customer info")
    def assert_account_customer_info(self):
        """Проверка учетной записи аккаунта"""
        self.click(self.ACCOUNT_LINKS)
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'My account - Customer info')
        self.assertions.assert_that_element_containce_text(self.YOUR_PERSONAL_DETAILS_TEXT, 'Your Personal Details')
        assert self.get_element(self.PERSONAL_DETAILS_FIRST_NAME)
        assert self.get_element(self.PERSONAL_DETAILS_LAST_NAME)
        self.save_screenshot('assert_account_customer_info.png')

    @allure.step("Password change on the user page")
    def password_change_on_the_user_page(self):
        """Смена пароля на странице пользователя"""
        self.click(self.ACCOUNT_LINKS)
        self.click(self.CHANGE_PASSWORD_BLOCK)
        self.fill(self.INTRODUCTION_OLD_PASSWORD, '123456Aabc')
        self.fill(self.INTRODUCTION_NEW_PASSWORD, '123456Aabca')
        self.fill(self.INTRODUCTION_CONFIRM_NEW_PASSWORD, '123456Aabca')
        self.click(self.CHANGE_PASSWORD_BUTTON)
        self.assertions.assert_that_element_containce_text(self.CHANGE_PASSWORD_MASSAGE, 'Password was changed')
        time.sleep(1)

        """Возвращаем старый пароль, чтобы тест на вход в аккаунт работал"""
        self.click(self.CHANGE_PASSWORD_BLOCK)
        self.fill(self.INTRODUCTION_OLD_PASSWORD, '123456Aabca')
        self.fill(self.INTRODUCTION_NEW_PASSWORD, '123456Aabc')
        self.fill(self.INTRODUCTION_CONFIRM_NEW_PASSWORD, '123456Aabc')
        self.click(self.CHANGE_PASSWORD_BUTTON)
        assert self.get_element(self.CHANGE_PASSWORD_BUTTON)
        self.assertions.assert_that_element_containce_text(self.CHANGE_PASSWORD_MASSAGE, 'Password was changed')
        time.sleep(1)

    @allure.step("Change password on page: incorrect entry of old password")
    def incorrect_entry_of_old_password(self):
        """Смена пароля на странице: неверный ввод старого пароля"""
        self.click(self.ACCOUNT_LINKS)
        self.click(self.CHANGE_PASSWORD_BLOCK)
        self.fill(self.INTRODUCTION_OLD_PASSWORD, 'asdfghjkl11111111111112222222')
        self.fill(self.INTRODUCTION_NEW_PASSWORD, '123456Aabca')
        self.fill(self.INTRODUCTION_CONFIRM_NEW_PASSWORD, '123456Aabca')
        self.click(self.CHANGE_PASSWORD_BUTTON)
        time.sleep(1)
        assert self.get_element(self.ERROR_CHANGE_PASSWORD_MASSAGE)

