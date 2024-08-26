#@allure.feature("Main feature")
#@allure.title("Test open shopping cart")
from pages import MainPage, WishlistLinkPage


def test_open_wishlist_link(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_wishlist()

    wishlist_link_page = WishlistLinkPage(driver)
    wishlist_link_page.assert_wishlist_page_is_opened()
