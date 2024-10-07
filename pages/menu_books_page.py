import time

import allure

from elements import HeaderMenu
from helpers.urls import MENU_BOOKS
from locators import MainLocators
from locators.menu_books_locators import MenuBooksLocators
from pages import BasePage


class MenuBooksPage(MenuBooksLocators, MainLocators, HeaderMenu, BasePage):

    def init(self, driver):
        super().__init__(driver)

    @allure.step("Open menu BOOKS")
    def open_menu_books(self):
        self.open_page(MENU_BOOKS)

    @allure.step("Checking the opening of the menu BOOKS")
    def assert_that_menu_books_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Books')
        assert self.get_element(self.PAGE_BODY)
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('menu_books_is_opened.png')

    @allure.step("Adding books to the cart through the showcase")
    def add_books_to_the_shopping_cart(self):
        self.click(self.BOOK_COMPUTING_AND_INTERNET_ADD_TO_CART)
        time.sleep(1)
        self.click(self.BOOK_FICTION_ADD_TO_CART)

    @allure.step("Remove books in shopping cart")
    def remove_books_in_shopping_cart(self):
        self.click(self.REMOVE_FROM_CART_BOOK_COMPUTING_AND_INTERNET)
        self.click(self.REMOVE_FROM_CART_BOOK_FICTION)

