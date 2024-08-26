import allure

from elements import HeaderLinks
from helpers import BASE_URL
from locators import MainLocators
from locators.shopping_cart_link_locators import ShoppingCartLinkLocators
from pages import BasePage


class ShoppingCartLinkPage(ShoppingCartLinkLocators, HeaderLinks, MainLocators, BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(BASE_URL)

#    @allure.step("Assert that page is opened")
    def assert_shopping_cart_page_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_SHOPPING_CART, 'Shopping cart')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
#        self.assertions.assert_that_element_containce_text(self.TEXT_BODY, 'Your Shopping Cart is empty!')

        self.save_screenshot('assert_shopping_cart_page_is_opened.png')
        allure.attach.file(
            "assert_shopping_cart_page_is_opened.png",
            name="assert_shopping_cart_page_is_opened",
            attachment_type=allure.attachment_type.PNG
        )