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

    def assert_wishlist_page_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Wishlist')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)

        self.save_screenshot('assert_wishlist_page_is_opened.png')
        allure.attach.file(
            "assert_wishlist_page_is_opened.png" ,
            name="assert_wishlist_page_is_opened" ,
            attachment_type=allure.attachment_type.PNG
        )

    def remove_item_from_wishlist(self):
        self.click(self.APPAREL_TOP_ITEM_PAGE)
        self.click(self.APPAREL_TOP_ADD_TO_WISHLIST_BUTTON)
        self.click(self.WISHLIST_UPPER_MENU)
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Wishlist')
        self.click(self.REMOVE_FROM_WISHLIST_CHECKBOX)
        self.click(self.UPDATE_WISHLIST)
        self.assertions.assert_that_element_containce_text(self.EMPTY_WISH_LIST_TEXT, 'The wishlist is empty!')

    def add_item_from_wishlist_to_cart(self):
        self.click(self.APPAREL_TOP_ITEM_PAGE)
        item_name = self.ITEM_NAME.
        self.click(self.APPAREL_TOP_ADD_TO_WISHLIST_BUTTON)
        self.click(self.WISHLIST_UPPER_MENU)
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Wishlist')
        item_wishlist_name = self.get_text(self.ITEM_POLKA_TOP_WISHLIST_NAME)
        self.click(self.ADD_TO_CART_FROM_WISHLIST_CHECKBOX)
        self.click(self.ADD_TO_CART_FROM_WISHLIST_BUTTON)
        item_cart_name = self.get_text(self.ITEM_POLKA_TOP_CART_NAME)
        assert item_name == item_wishlist_name == item_cart_name