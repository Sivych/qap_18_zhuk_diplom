import allure
import random
from generator.generator import generated_new_user

from elements import HeaderLinks
from helpers import BASE_URL
from locators import RegisterLinkLocators, MainLocators
from pages import BasePage


class RegisterLinkPage(RegisterLinkLocators, HeaderLinks, MainLocators, BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Checking the opening of the register page")
    def assert_register_page_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Register')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('register_page_is_opened.png')

    @allure.step("Registration with empty values")
    def validation_message(self):
        """Регистрация с вводом пустых значений"""
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIRST_NAME_VALIDATION_ERROR, 'First name is required.')
        self.assertions.assert_that_element_containce_text(self.LAST_NAME_VALIDATION_ERROR, 'Last name is required.')
        self.assertions.assert_that_element_containce_text(self.EMAIL_VALIDATION_ERROR, 'Email is required.')
        self.assertions.assert_that_element_containce_text(self.PASSWORD_VALIDATION_ERROR, 'Password is required.')
        self.assertions.assert_that_element_containce_text(self.CONFIRM_PASSWORD_VALIDATION_ERROR, 'Password is required.')

        self.save_screenshot('validation_message.png')

    @allure.step("New user registration")
    def randon_new_user_input_data(self):
        """Регистрация нового пользователя"""
        gender_list = self.get_elements(self.GENDER_LIST)
        gender_button = gender_list[random.randint(0, 1)]
        self.go_to_element(gender_button)
        gender_button.click()
        user_info = next(generated_new_user())
        self.fill(self.FIRST_NAME, user_info.first_name)
        self.fill(self.LAST_NAME, user_info.last_name)
        self.fill(self.EMAIL, user_info.email)
        self.fill(self.PASSWORD, '123456')
        self.fill(self.CONFIRM_PASSWORD, '123456')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.COMPLETED_REGISTRATION_TEXT ,
                                                           'Your registration completed')

    @allure.step("Registration without entering email")
    def empty_email_field(self):
        """Проверка email на валидность: оставить пустое поле Email"""
        gender_list = self.get_elements(self.GENDER_LIST)
        gender_button = gender_list[random.randint(0, 1)]
        self.go_to_element(gender_button)
        gender_button.click()
        user_info = next(generated_new_user())
        self.fill(self.FIRST_NAME, user_info.first_name)
        self.fill(self.LAST_NAME, user_info.last_name)
        self.fill(self.PASSWORD, '123456')
        self.fill(self.CONFIRM_PASSWORD, '123456')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.EMAIL_VALIDATION_ERROR, 'Email is required.')
        self.save_screenshot('validation_message_email.png')

    @allure.step("Checking email name for validity")
    def check_email_name_for_validity(self, successful_email):
        """Проверка email на валидность: Email в нижнем и верхнем регистре,
        Email с цифрами в имени аккаунта, Email с дефисом в имени аккаунта,
        Email со знаком подчеркивания в имени аккаунта, Email с точками в имени аккаунта"""
        self.fill(self.EMAIL, successful_email)
        self.click_on_register_button()
        # time.sleep(1)
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @allure.step("Checked the validity of the email domain part")
    def check_valid_email_in_domain(self, successful_email_domain):
        """Проверка email на валидность: Email с цифрами в доменной части, с дефисом,
        со знаком подчеркивания, с несколькими точками в доменной части"""
        self.fill(self.EMAIL, successful_email_domain)
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @allure.step("Registration where Email exceeding the length (> 320 characters)")
    def check_valid_email_exceeding_the_length(self):
        """Проверка email на валидность: Превышение длины email (>320 символов)"""
        self.fill(self.EMAIL, 'Petrova.Alinaaaaaaaaaaaaaaaaaaaaa'
                               'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                               'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                               'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                               'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                               'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                               'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                               'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                               'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                               'aaaaaaaaa@mail.com')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @allure.step("Сheck for invalid email impassability")
    def check_invalid_email_impassability(self, invalid_email):
        """Проверка на непроходимость невалидного эмейла:
        Email без точек в доменной части,
        отсутствие @ в email,
        Email с пробелами в имени аккаунта, с пробелами в доменной части,
        Email без имени аккаунта, Email без доменной части"""
        self.fill(self.EMAIL, invalid_email)
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL,
                                                           'Wrong email')
