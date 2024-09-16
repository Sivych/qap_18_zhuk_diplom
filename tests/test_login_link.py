import allure

from pages import MainPage
from pages.login_link_page import LoginLinkPage


@allure.feature("Header Links")
@allure.title("Open Lod in")
def test_open_login_link(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_login()

    login_link_page = LoginLinkPage(driver)
    login_link_page.assert_login_page_is_opened()


@allure.feature("Header Links")
@allure.title("User authorization")
def test_user_authorization(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_login()

    login_link_page = LoginLinkPage(driver)
    login_link_page.user_authorization()


@allure.feature("Header Links")
@allure.title("Error user authorization")
def test_error_user_authorization(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_login()

    login_link_page = LoginLinkPage(driver)
    login_link_page.error_user_authorization()


