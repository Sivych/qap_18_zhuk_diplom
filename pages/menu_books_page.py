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

    #    @allure.step("Assert that page is opened")
    def assert_that_menu_books_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Books')
#        self.assertions.assert_that_element_containce_text(self.TEXT_SORT_BY, 'Sort by')
        assert self.get_element(self.FOOTER_MENU_WRAPPER)


    # def assert_add_books_to_the_shopping_cart(self):



