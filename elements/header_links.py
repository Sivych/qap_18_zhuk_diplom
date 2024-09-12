from locators import HeaderLinksLocators
from pages import BasePage


class HeaderLinks(BasePage, HeaderLinksLocators):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_shopping_cart(self):
        self.click(self.SHOPPING_CART_MENU_BUTTON)

    def click_on_register(self):
        self.click(self.REGISTER_MENU_BUTTON)

    def click_on_login(self):
        self.click(self.LOGIN_MENU_BUTTON)

    def click_on_wishlist(self):
        self.click(self.WISHLIST_MENU_BUTTON)

    def click_on_register_button(self):
        self.click(self.REGISTER_BUTTON)

    def click_on_login_button(self):
        self.click(self.LOGIN_BUTTON)
