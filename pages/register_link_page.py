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
        self.assertions.assert_that_element_containce_text(self.COMPLETED_REGISTRATION_TEXT,
                                                           'Your registration completed')

    @allure.step("Registration with dataset")
    def registration_with_dataset(self):
        gender_list = self.get_elements(self.GENDER_LIST)
        gender_button = gender_list[1]
        self.go_to_element(gender_button)
        gender_button.click()
        self.fill(self.FIRST_NAME, 'Kristina')
        self.fill(self.LAST_NAME, 'Zhuk')
        self.fill(self.EMAIL, 'KZhuk111@mail.com')
        self.fill(self.PASSWORD, '123456Aabc')
        self.fill(self.CONFIRM_PASSWORD, '123456Aabc')
        time.sleep(5)
        self.click_on_register_button()
        time.sleep(5)
        self.assertions.assert_that_element_containce_text(self.COMPLETED_REGISTRATION_TEXT,
                                                           'Your registration completed')

