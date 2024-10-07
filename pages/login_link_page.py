import allure
import time

from generator.data import DatasetLogin
from generator.generator import generated_new_user

from elements import HeaderLinks
from helpers.urls import LOGIN_URL
from locators import MainLocators, LoginLinkLocators, RegisterLinkLocators
from pages import BasePage


class LoginLinkPage(DatasetLogin, LoginLinkLocators, RegisterLinkLocators, HeaderLinks, MainLocators, BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Open page Login")
    def open_login_link(self):
        self.open_page(LOGIN_URL)

    @allure.step("Checking the opening of the login page")
    def assert_login_page_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Welcome, Please Sign In!')
        assert self.get_elements(self.ACCOUNT_LOGIN_WINDOW)
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('login_page_is_opened.png')

    @allure.step("Login to ready data")
    def login_to_ready_data(self):
        """Вход в аккаунт с готовыми данными"""
        self.fill(self.EMAIL, self.dataset_email)
        self.fill(self.PASSWORD, self.dataset_password)
        self.click_on_login_button()

    @allure.step("Checking login on the ready data")
    def checking_login_on_the_ready_data(self):
        assert self.get_element(self.HEADER_LOGO)
        assert self.get_element(self.HEADER_MENU)
        assert self.get_element(self.SLIDER)
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('successful_user_authorization.png')

    @allure.step("Login with non existent data")
    def login_with_non_existent_data(self):
        """Вход с несуществующими данными"""
        user_info = next(generated_new_user())
        email = user_info.email
        self.fill(self.EMAIL, email)
        self.fill(self.PASSWORD, '123456Aabc')
        self.click_on_login_button()

    @allure.step("Login check on non-existent data")
    def login_check_non_existent_data(self):
        """Проверка входа на несуществующих данных"""
        assert self.get_element(self.VALIDATION_SUMMARY_ERRORS)
        self.save_screenshot('error_user_authorization.png')

    @allure.step("Account verification")
    def assert_account_customer_info(self):
        """Проверка учетной записи аккаунта"""
        self.click(self.ACCOUNT_LINKS)
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'My account - Customer info')
        self.assertions.assert_that_element_containce_text(self.YOUR_PERSONAL_DETAILS_TEXT, 'Your Personal Details')
        assert self.get_element(self.PERSONAL_DETAILS_FIRST_NAME)
        assert self.get_element(self.PERSONAL_DETAILS_LAST_NAME)
        self.save_screenshot('account_verification.png')

    @allure.step("Password change on the user page")
    def password_change_on_the_user_page(self):
        """Смена пароля на странице пользователя"""
        self.click(self.ACCOUNT_LINKS)
        self.click(self.CHANGE_PASSWORD_BLOCK)
        self.fill(self.INTRODUCTION_OLD_PASSWORD, '123456Aabc')
        self.fill(self.INTRODUCTION_NEW_PASSWORD, '123456Aabca')
        self.fill(self.INTRODUCTION_CONFIRM_NEW_PASSWORD, '123456Aabca')
        self.click(self.CHANGE_PASSWORD_BUTTON)
        time.sleep(1)

        """Возвращаем старый пароль, чтобы тест на вход в аккаунт работал"""
        self.click(self.CHANGE_PASSWORD_BLOCK)
        self.fill(self.INTRODUCTION_OLD_PASSWORD, '123456Aabca')
        self.fill(self.INTRODUCTION_NEW_PASSWORD, '123456Aabc')
        self.fill(self.INTRODUCTION_CONFIRM_NEW_PASSWORD, '123456Aabc')
        self.click(self.CHANGE_PASSWORD_BUTTON)

    @allure.step("Check for successful password change")
    def check_for_successful_password_change(self):
        """Проверка на успешную смену пароля на странице пользователя"""
        assert self.get_element(self.CHANGE_PASSWORD_BUTTON)
        self.assertions.assert_that_element_containce_text(self.CHANGE_PASSWORD_MASSAGE, 'Password was changed')
        self.save_screenshot('successful_password_change.png')

    @allure.step("Change password on page: incorrect entry of old password")
    def incorrect_entry_of_old_password(self):
        """Смена пароля на странице: неверный ввод старого пароля"""
        self.click(self.ACCOUNT_LINKS)
        self.click(self.CHANGE_PASSWORD_BLOCK)
        self.fill(self.INTRODUCTION_OLD_PASSWORD, 'asdfghjkl11111111111112222222')
        self.fill(self.INTRODUCTION_NEW_PASSWORD, '123456Aabca')
        self.fill(self.INTRODUCTION_CONFIRM_NEW_PASSWORD, '123456Aabca')
        self.click(self.CHANGE_PASSWORD_BUTTON)

    @allure.step("Check for incorrect entry of old password")
    def check_for_incorrect_entry_of_old_password(self):
        """Проверка на неверный ввод старого пароля"""
        assert self.get_element(self.ERROR_CHANGE_PASSWORD_MASSAGE)
        self.save_screenshot('error_password_change.png')
