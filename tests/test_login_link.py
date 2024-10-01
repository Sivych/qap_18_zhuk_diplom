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


@allure.feature("Header Links")
@allure.title("Assert account customer info")
def test_open_account_customer_info(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_login()

    login_link_page = LoginLinkPage(driver)
    login_link_page.user_authorization()

    login_link_page.assert_account_customer_info()


@allure.feature("Header Links")
@allure.title("Password change on the user page")
def test_password_change_on_the_user_page(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_login()

    login_link_page = LoginLinkPage(driver)
    login_link_page.user_authorization()

    login_link_page.password_change_on_the_user_page()


@allure.feature("Header Links")
@allure.title("Change password on page: incorrect entry of old password")
def test_incorrect_entry_of_old_password(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_login()

    login_link_page = LoginLinkPage(driver)
    login_link_page.user_authorization()

    login_link_page.incorrect_entry_of_old_password()




