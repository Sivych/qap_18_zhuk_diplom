from helpers.assertions import Assertions
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        self.assertions = Assertions(driver)

    def open_page(self, url):
        self.driver.get(url)

    def click(self, selector):
        element = self.driver.find_element(*selector)
        element.click()

    def clear(self, selector):
        element = self.driver.find_element(*selector)
        element.clear()

    def fill(self, selector, text):
        element = self.driver.find_element(*selector)
        element.send_keys(text)

    def get_element(self, selector):
        return self.driver.find_element(*selector)

    def get_elements(self, selector):
        return self.driver.find_elements(*selector)

    def add_cookie(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.add_cookie(cookie)

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)
        allure.attach.file(
            name,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def get_text(self, selector):
        element = self.driver.find_element(*selector)
        return element.text

    def go_to_element(self, value):
        self.driver.execute_script("arguments[0].scrollIntoView();", value)