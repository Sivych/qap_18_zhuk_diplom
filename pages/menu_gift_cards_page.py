import allure

from elements import HeaderMenu
from helpers.urls import MENU_GIFT_CARDS
from locators import MainLocators
from pages import BasePage


class MenuGiftCardsPage(MainLocators, HeaderMenu, BasePage):

    def init(self, driver):
        super().__init__(driver)

    @allure.step("Open menu GIFT CARDS")
    def open_menu_gift_cards(self):
        self.open_page(MENU_GIFT_CARDS)

    @allure.step("Checking the opening of the menu GIFT CARDS")
    def assert_that_menu_gift_cards_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Gift Cards')
        assert self.get_element(self.PAGE_BODY)
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('menu_gift_cards_is_opened.png')