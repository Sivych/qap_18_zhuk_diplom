import time
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

    def open(self):
        self.driver.get(BASE_URL)

    @allure.step("Assert register page is opened")
    def assert_register_page_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Register')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)

        self.save_screenshot('assert_register_page_is_opened.png')
        allure.attach.file(
            "assert_register_page_is_opened.png",
            name="assert_register_page_is_opened",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Validation message")
    def validation_message(self):
        """Регистрация с вводом пустых значений"""
        self.assertions.assert_that_element_containce_text(self.FIRST_NAME_VALIDATION_ERROR, 'First name is required.')
        self.assertions.assert_that_element_containce_text(self.LAST_NAME_VALIDATION_ERROR, 'Last name is required.')
        self.assertions.assert_that_element_containce_text(self.EMAIL_VALIDATION_ERROR, 'Email is required.')
        self.assertions.assert_that_element_containce_text(self.PASSWORD_VALIDATION_ERROR, 'Password is required.')
        self.assertions.assert_that_element_containce_text(self.CONFIRM_PASSWORD_VALIDATION_ERROR, 'Password is required.')

        self.save_screenshot('validation_message.png')
        allure.attach.file(
            "validation_message.png",
            name="validation_message",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Random new user input data")
    def randon_new_user_input_data(self):
        """Регистрация нового пользователя"""
        gender_list = self.get_elements(self.GENDER_LIST)
        gender_button = gender_list[random.randint(0, 1)]
        self.go_to_element(gender_button)
        gender_button.click()
        user_info = next(generated_new_user())
        first_name = user_info.first_name
        last_name = user_info.last_name
        email = user_info.email
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.EMAIL, email)
        self.fill(self.PASSWORD, '123456')
        self.fill(self.CONFIRM_PASSWORD, '123456')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.COMPLETED_REGISTRATION_TEXT ,
                                                           'Your registration completed')

    @allure.step("Empty email field")
    def empty_email_field(self):
        """Проверка email на валидность: оставить пустое поле Email"""
        gender_list = self.get_elements(self.GENDER_LIST)
        gender_button = gender_list[random.randint(0, 1)]
        self.go_to_element(gender_button)
        gender_button.click()
        user_info = next(generated_new_user())
        first_name = user_info.first_name
        last_name = user_info.last_name
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.PASSWORD, '123456')
        self.fill(self.CONFIRM_PASSWORD, '123456')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.EMAIL_VALIDATION_ERROR, 'Email is required.')
        self.save_screenshot('validation_message_email.png')
        allure.attach.file(
            "validation_message_email.png",
            name="validation_message_email",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Email in lowercase")
    def email_in_lowercase(self):
        """Проверка email на валидность: Email в нижнем регистре"""
        self.fill(self.EMAIL, 'asfgrwqet@mail.ru')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @allure.step("Email in uppercase")
    def email_in_uppercase(self):
        """Проверка email на валидность: Email в верхнем регистре"""
        self.fill(self.EMAIL, 'PETROVA@mail.ru')
        self.click_on_register_button()
        time.sleep(1)
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @allure.step("Email with numbers in the account name")
    def email_with_numbers(self):
        """Проверка email на валидность: Email с цифрами в имени аккаунта"""
        self.fill(self.EMAIL, '123456789@mail.ru')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @allure.step("Email with numbers in the domain part")
    def email_with_numbers_in_domain(self):
        """Проверка email на валидность: Email с цифрами в доменной части"""
        self.fill(self.EMAIL, 'PETROVA@1234.com')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @allure.step("Email with a hyphen in the account name")
    def email_with_hyphen(self):
        """Проверка email на валидность: Email с дефисом в имени аккаунта"""
        self.fill(self.EMAIL, 'Petrova-Alina@1234.com')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @allure.step("Email with a hyphen in the domain part")
    def email_with_hyphen_in_domain(self):
        """Проверка email на валидность: Email с дефисом в доменной части"""
        self.fill(self.EMAIL, 'Petrova-Alina@strange-example.com')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @allure.step("Email with underscore in account name")
    def email_with_underscore(self):
        """Проверка email на валидность: Email со знаком подчеркивания в имени аккаунта"""
        self.fill(self.EMAIL, 'Petrova_Alina@mail.com')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @allure.step("Email with underscore in the domain part")
    def email_with_underscore_in_domain(self):
        """Проверка email на валидность: Email со знаком подчеркивания в доменной части"""
        self.fill(self.EMAIL, 'PetrovaAlina@strange_example.com')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @ allure.step("Email with dots in account name")
    def email_with_dots(self):
        """Проверка email на валидность: Email с точками в имени аккаунта"""
        self.fill(self.EMAIL, 'Petrova.Alina@mail.com')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @allure.step("Email with multiple dots in the domain part")
    def email_with_dots_in_domain(self):
        """Проверка email на валидность: Email с несколькими точками в доменной части"""
        self.fill(self.EMAIL, 'Petrova.Alina@strange.example.com')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL, '')

    @allure.step("Email without points in the domain part")
    def email_without_points_in_domain(self):
        """Проверка email на валидность: Email без точек в доменной части"""
        self.fill(self.EMAIL, 'Petrova.Alina@strange_examplecom')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL,
                                                           'Wrong email')

    @allure.step("Email exceeding the length (> 320 characters)")
    def email_exceeding_the_length(self):
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

    @allure.step("Lack @ in email")
    def lack_commercial_at_in_email(self):
        """Проверка email на валидность: Отсутствие @ в email"""
        self.fill(self.EMAIL, 'Petrova.Alina.strange_example.com')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL,
                                                           'Wrong email')

    @allure.step("Email with spaces in the name of the account")
    def email_with_spaces(self):
        """Проверка email на валидность: Email с пробелами в имени аккаунта"""
        self.fill(self.EMAIL, 'Petrova Alina@strange_example.com')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL,
                                                           'Wrong email')

    @allure.step("Email with spaces in the domain part")
    def email_with_spaces_in_domain(self):
        """Проверка email на валидность: Email с пробелами в доменной части"""
        self.fill(self.EMAIL, 'Petrova Alina@strange_example.com')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL,
                                                           'Wrong email')

    @allure.step("Email without an account")
    def email_without_an_account(self):
        """Проверка email на валидность: Email без имени аккаунта"""
        self.fill(self.EMAIL, '@gmail.com')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL,
                                                           'Wrong email')

    @allure.step("Email without domain")
    def email_without_domain(self):
        """Проверка email на валидность: Email без доменной части"""
        self.fill(self.EMAIL, 'Petrova_Alina')
        self.click_on_register_button()
        self.assertions.assert_that_element_containce_text(self.FIELD_VALIDATION_ERROR_EMAIL,
                                                           'Wrong email')