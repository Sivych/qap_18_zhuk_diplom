#@allure.feature("Main feature")
#@allure.title("Test open shopping cart")
from pages import MainPage
from pages.register_link_page import RegisterLinkPage


def test_open_register_link(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.assert_register_page_is_opened()
