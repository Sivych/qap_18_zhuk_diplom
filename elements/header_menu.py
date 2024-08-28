from locators import HeaderMenuLocators
from pages import BasePage


class HeaderMenu(BasePage, HeaderMenuLocators):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_menu_books(self):
        self.click(self.MENU_BOOKS)

    def click_on_menu_computers(self):
        self.click(self.MENU_COMPUTERS)

    def click_on_menu_electronics(self):
        self.click(self.MENU_ELECTRONICS)

    def click_on_menu_apparel_shoes(self):
        self.click(self.MENU_APPAREL_SHOES)

    def click_on_menu_digital_downloads(self):
        self.click(self.MENU_DIGITAL_DOWNL)

    def click_on_menu_jewelry(self):
        self.click(self.MENU_JEWELRY)

    def click_on_menu_gift_cards(self):
        self.click(self.MENU_GIFT_CARDS)