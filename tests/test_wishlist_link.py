import allure
from pages import MainPage, WishlistLinkPage


@allure.feature("Header Links")
@allure.title("Open wishlist link")
def test_open_wishlist_link(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_wishlist()

    wishlist_link_page = WishlistLinkPage(driver)
    wishlist_link_page.assert_wishlist_page_is_opened()


@allure.feature("Header Links")
@allure.title("Remove item from wishlist")
def test_remove_item_from_wishlist(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_menu_apparel_shoes()

    wishlist_link_page = WishlistLinkPage(driver)
    wishlist_link_page.remove_item_from_wishlist()


@allure.feature("Header Links")
@allure.title("Add item from wishlist to cart")
def test_add_item_from_wishlist_to_cart(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_menu_apparel_shoes()

    wishlist_link_page = WishlistLinkPage(driver)
    wishlist_link_page.add_item_from_wishlist_to_cart()
