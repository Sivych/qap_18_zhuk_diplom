import allure

from elements import HeaderMenu
from helpers import BASE_URL
from locators import MainLocators
from locators.menu_books_locators import MenuBooksLocators
from pages import BasePage


class MenuBooksPage(MenuBooksLocators, MainLocators, HeaderMenu, BasePage):

    def init(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(BASE_URL)

    @allure.step("Assert that menu books is opened")
    def assert_that_menu_books_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Books')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)

    @allure.step("Add books to the shopping cart via the showcase")
    def add_books_to_the_shopping_cart(self):
        self.click(self.BOOK_COMPUTING_AND_INTERNET_ADD_TO_CART)
        self.click(self.BOOK_FICTION_ADD_TO_CART)



