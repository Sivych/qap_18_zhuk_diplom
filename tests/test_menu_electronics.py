import allure
import time
from pages import MainPage, ShoppingCartLinkPage
from pages.menu_electronics_page import MenuElectronicsPage


@allure.feature("Header menu Electronics")
class TestsHeaderMenuElectronics:

    @allure.title("Check phone cover options")
    def test_check_phone_cover_options(self, driver):
        electronics_menu_page = MenuElectronicsPage(driver)
        electronics_menu_page.open_menu_electronics()
        electronics_menu_page.check_phone_cover_options()

    @allure.title("Checking if Phone Cover is in Cart")
    def test_checking_if_phone_cover_is_in_cart(self, driver):
        main_page = MainPage(driver)
        electronics_menu_page = MenuElectronicsPage(driver)
        electronics_menu_page.open_menu_electronics()
        electronics_menu_page.add_phone_cover_to_cart()
        time.sleep(2)
        main_page.click_on_shopping_cart()
        shopping_cart_link_page = ShoppingCartLinkPage(driver)
        shopping_cart_link_page.assert_shopping_cart_page_is_opened()
        electronics_menu_page.checking_if_phone_cover_is_in_cart()

    @allure.title("Check for negative quantity input smartphone")
    def test_check_negative_qty_values_smartphone(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_menu_electronics()

        electronics_menu_page = MenuElectronicsPage(driver)
        electronics_menu_page.add_negative_qty_values_smartphone()
        time.sleep(2)
        electronics_menu_page.check_for_negative_quantity_input()

    @allure.title("Checking for limit values input smartphone")
    def test_check_over_limit_qty_values_smartphone(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_menu_electronics()

        electronics_menu_page = MenuElectronicsPage(driver)
        electronics_menu_page.add_over_limit_qty_values_smartphone()
        time.sleep(2)
        electronics_menu_page.checking_for_limit_values_input()