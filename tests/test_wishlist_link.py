import allure
import time

from pages import MainPage, WishlistLinkPage
from pages.menu_apparel_shoes_page import MenuApparelShoesPage


@allure.feature("Header link Wishlist")
class TestsHeaderLinkWishlist:
    @allure.title("Opening wishlist link page")
    def test_open_wishlist_link(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_wishlist()

        wishlist_link_page = WishlistLinkPage(driver)
        wishlist_link_page.assert_wishlist_page_is_opened()

    @allure.title("Remove item from wishlist")
    def test_remove_item_from_wishlist(self, driver):
        apparel_shoes_menu_page = MenuApparelShoesPage(driver)
        apparel_shoes_menu_page.open_menu_apparel_shoes()
        apparel_shoes_menu_page.add_apparel_to_the_wishlist()
        time.sleep(1)

        wishlist_link_page = WishlistLinkPage(driver)

        main_page = MainPage(driver)
        main_page.click_on_wishlist()

        wishlist_link_page.remove_item_from_wishlist()
        wishlist_link_page.checking_remove_item_from_wishlist()

    @allure.title("Add item from wishlist to cart")
    def test_add_item_from_wishlist_to_cart(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_menu_apparel_shoes()

        wishlist_link_page = WishlistLinkPage(driver)
        wishlist_link_page.add_item_from_wishlist_to_cart()
