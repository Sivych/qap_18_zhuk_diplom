#@allure.feature("Main feature")
#@allure.title("Test open shopping cart")
from pages import MainPage
from pages.shopping_cart_link_page import ShoppingCartLinkPage


def test_open_shopping_cart(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_shopping_cart()

    shopping_cart_link_page = ShoppingCartLinkPage(driver)
    shopping_cart_link_page.assert_shopping_cart_page_is_opened()
