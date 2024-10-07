import time
import allure

from elements import HeaderLinks, HeaderMenu
from locators import MainLocators, WishlistLinkLocators, MenuApparelShoesLocators
from pages import BasePage


class WishlistLinkPage(WishlistLinkLocators, MenuApparelShoesLocators, HeaderLinks, HeaderMenu, MainLocators, BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Checking the opening of the wishlist page")
    def assert_wishlist_page_is_opened(self):
        """Избранное открыто"""
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Wishlist')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('wishlist_page_is_opened.png')

    @allure.step("Remove product in wishlist")
    def remove_item_from_wishlist(self):
        """Удаляем товар из избранного"""
        self.click(self.REMOVE_FROM_WISHLIST_CHECKBOX)
        self.click(self.UPDATE_WISHLIST)

    @allure.step("Checking if a product has been removed from wishlist")
    def checking_remove_item_from_wishlist(self):
        """Проверяем удаляется ли товар из избранного"""
        self.assertions.assert_that_element_containce_text(self.EMPTY_WISH_LIST_TEXT, 'The wishlist is empty!')

    @allure.step("Add item from wishlist to cart")
    def add_item_from_wishlist_to_cart(self):
        """ Добавляем товар из избранного в корзину"""
        self.click(self.APPAREL_TOP_ITEM_PAGE)
        item_name = self.get_text(self.ITEM_NAME)
        self.click(self.APPAREL_TOP_ADD_TO_WISHLIST_BUTTON)
        time.sleep(1)
        self.click(self.WISHLIST_UPPER_MENU)
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Wishlist')
        item_wishlist_name = self.get_text(self.ITEM_POLKA_TOP_WISHLIST_NAME)
        self.click(self.ADD_TO_CART_FROM_WISHLIST_CHECKBOX)
        self.click(self.ADD_TO_CART_FROM_WISHLIST_BUTTON)
        item_cart_name = self.get_text(self.ITEM_POLKA_TOP_CART_NAME)
        assert item_name == item_wishlist_name == item_cart_name