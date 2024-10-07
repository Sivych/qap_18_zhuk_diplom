import allure

from elements import HeaderLinks
from helpers import BASE_URL
from locators import MainLocators
from locators.shopping_cart_link_locators import ShoppingCartLinkLocators
from pages import BasePage


class ShoppingCartLinkPage(ShoppingCartLinkLocators, HeaderLinks, MainLocators, BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Checking the opening of the shopping_cart page")
    def assert_shopping_cart_page_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_SHOPPING_CART, 'Shopping cart')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)

        self.save_screenshot('shopping_cart_page_is_opened.png')

    @allure.step("Checkout in the shopping cart")
    def checkout_in_the_shopping_cart(self):
        """Оформление заказа в корзине"""
        self.click(self.TERMS_OF_SERVICE)
        self.click(self.CHECKOUT_BUTTON)

    @allure.step("Checking the order processing without authorization")
    def checking_the_order_processing_without_authorization(self):
        """Проверка работы оформления заказа без авторизации: перевод на страницу логина"""
        assert self.get_text(self.CHECKOUT_GUEST_OR_REGISTER_TEXT)

    @allure.step("Сleaning shopping cart")
    def cleaning_shopping_cart(self):
        """Очистка корзины"""
        self.click(self.UPDATE_SHOPPING_CART_BUTTON)
