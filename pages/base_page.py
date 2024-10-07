from helpers.assertions import Assertions

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException


import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        self.assertions = Assertions(driver)

    @allure.step('Open page')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Click')
    def click(self, selector):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(selector)
            ).click()

        except (NoSuchElementException, TimeoutException):
            assert False, f"Element {selector} does not find"

    @allure.step('Clear')
    def clear(self, selector):
        element = self.driver.find_element(*selector)
        element.clear()

    @allure.step('Fill field with text')
    def fill(self, selector, text):
        element = self.driver.find_element(*selector)
        element.send_keys(text)

    @allure.step('Get element')
    def get_element(self, selector):
        try:
            return WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(selector)
            )

        except (NoSuchElementException, TimeoutException):
            assert False, f"Element {selector} does not find"

    @allure.step('Get elements')
    def get_elements(self, selector):
        try:
            return WebDriverWait(self.driver, 30).until(
                EC.visibility_of_all_elements_located(selector)
            )

        except (NoSuchElementException, TimeoutException):
            assert False, f"Elements {selector} does not find"

    # def add_cookie(self, name, value):
    #     cookie = {'name': name, 'value': value}
    #     self.driver.add_cookie(cookie)

    @allure.step('Save screenshot')
    def save_screenshot(self, name):
        self.driver.save_screenshot(name)
        allure.attach.file(
            name,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step('Get text')
    def get_text(self, selector):
        element = self.driver.find_element(*selector)
        return element.text

    @allure.step('Go to element')
    def go_to_element(self, value):
        self.driver.execute_script("arguments[0].scrollIntoView();", value)