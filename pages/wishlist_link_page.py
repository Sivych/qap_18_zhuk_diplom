import time
import allure

from elements import HeaderLinks, HeaderMenu
from helpers import BASE_URL
from locators import MainLocators, WishlistLinkLocators, MenuApparelShoesLocators
from pages import BasePage


class WishlistLinkPage(WishlistLinkLocators, MenuApparelShoesLocators, HeaderLinks, HeaderMenu, MainLocators, BasePage):
    def __init__(self , driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(BASE_URL)

    @allure.step("Assert wishlist page is opened")
    def assert_wishlist_page_is_opened(self):
        """Избранное открыто"""
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Wishlist')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)

        self.save_screenshot('assert_wishlist_page_is_opened.png')
        allure.attach.file(
            "assert_wishlist_page_is_opened.png" ,
            name="assert_wishlist_page_is_opened" ,
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Remove item from wishlist")
    def remove_item_from_wishlist(self):
        """ Добавляем товар в избранное и проверяем удаляется ли он из неё"""
        self.click(self.APPAREL_TOP_ITEM_PAGE)
        self.click(self.APPAREL_TOP_ADD_TO_WISHLIST_BUTTON)
        time.sleep(1)
        self.click(self.WISHLIST_UPPER_MENU)
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Wishlist')
        self.click(self.REMOVE_FROM_WISHLIST_CHECKBOX)
        self.click(self.UPDATE_WISHLIST)
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