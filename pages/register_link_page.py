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

#    @allure.step("Assert that page is opened")
    def assert_register_page_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Register')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)

        self.save_screenshot('assert_register_page_is_opened.png')
        allure.attach.file(
            "assert_register_page_is_opened.png",
            name="assert_register_page_is_opened",
            attachment_type=allure.attachment_type.PNG
        )

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

    def new_user_input_data(self):
        gender_list = self.get_element(self.GENDER_LIST)
        gender_button = gender_list[random.randint(0 , 1)]
        self.go_to_element(gender_button)
        gender_button.click()
        user_info = next(generated_new_user())
        first_name = user_info.first_name
        last_name = user_info.last_name
        email = user_info.email
        first_name.fill(self.FIRST_NAME)
        last_name.fill(self.LAST_NAME)
        email.fill(self.EMAIL)
        password = self.driver.find_element('PASSWORD')
        password.fill(self.)

        element = self.driver.find_element(selector)
        element.send_keys(text)


        self.assert_that_element_is_visible(self.FIRST_NAME)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.PASSWORD).send_keys('123456')
        self.element_is_visible(self.locators.CONFIRM_PASSWORD).send_keys('123456')

        self.element_is_visible(self.locators.REGISTER_BUTTON).click()

        self.assertions.assert_that_element_containce_text(self.COMPLETED_REGISTRATION_TEXT, ' ')
