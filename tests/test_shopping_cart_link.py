import allure
import time
from pages import MainPage , MenuElectronicsPage , LoginLinkPage , MenuBooksPage
from pages.shopping_cart_link_page import ShoppingCartLinkPage


@allure.feature("Header link Shopping cart")
class TestsHeaderLinkShoppingCart:
    @allure.title("Open shopping cart")
    def test_open_shopping_cart(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_shopping_cart()

        shopping_cart_link_page = ShoppingCartLinkPage(driver)
        shopping_cart_link_page.assert_shopping_cart_page_is_opened()

    @allure.title("Checking the order processing without authorization")
    def test_checking_the_order_processing_without_authorization(self, driver):
        electronics_menu_page = MenuElectronicsPage(driver)
        electronics_menu_page.open_menu_electronics()
        electronics_menu_page.add_phone_cover_to_cart()
        time.sleep(1)

        main_page = MainPage(driver)
        main_page.click_on_shopping_cart()
        electronics_menu_page.checking_if_phone_cover_is_in_cart()

        shopping_cart_link_page = ShoppingCartLinkPage(driver)
        shopping_cart_link_page.checkout_in_the_shopping_cart()

        login_link_page = LoginLinkPage(driver)
        login_link_page.assert_login_page_is_opened()
        shopping_cart_link_page.checking_the_order_processing_without_authorization()

    @allure.step("Checking cleaning shopping cart")
    def test_checking_cleaning_shopping_cart(self, driver):
        books_menu_page = MenuBooksPage(driver)
        books_menu_page.open_menu_books()
        books_menu_page.add_books_to_the_shopping_cart()
        time.sleep(1)

        main_page = MainPage(driver)
        main_page.click_on_shopping_cart()

        books_menu_page.remove_books_in_shopping_cart()

        shopping_cart_link_page = ShoppingCartLinkPage(driver)
        shopping_cart_link_page.assert_shopping_cart_page_is_opened()