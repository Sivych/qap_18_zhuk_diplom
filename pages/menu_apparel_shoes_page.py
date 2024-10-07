import allure

from elements import HeaderMenu
from helpers.urls import MENU_APPAREL_SHOES
from locators import MainLocators, MenuApparelShoesLocators
from pages import BasePage


class MenuApparelShoesPage(MenuApparelShoesLocators, MainLocators, HeaderMenu, BasePage):

    def init(self, driver):
        super().__init__(driver)

    @allure.step("Open menu APPAREL & SHOES")
    def open_menu_apparel_shoes(self):
        self.open_page(MENU_APPAREL_SHOES)

    @allure.step("Checking the opening of the menu APPAREL & SHOES")
    def assert_that_menu_apparel_shoes_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Apparel & Shoes')
        assert self.get_element(self.PAGE_BODY)
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('menu_apparel_shoes_is_opened.png')

    @allure.step("Adding apparel to the Wishlist")
    def add_apparel_to_the_wishlist(self):
        self.click(self.APPAREL_TOP_ITEM_PAGE)
        self.click(self.APPAREL_TOP_ADD_TO_WISHLIST_BUTTON)