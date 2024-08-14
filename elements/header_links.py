from locators import HeaderLinksLocators
from pages import BasePage


class HeaderLinks(BasePage, HeaderLinksLocators):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_shopping_cart(self):
        self.click(self.SHOPPING_CART)
