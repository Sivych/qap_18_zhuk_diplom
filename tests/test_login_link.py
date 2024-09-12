import allure

from pages import MainPage
from pages.login_link_page import LoginLinkPage
from pages.register_link_page import RegisterLinkPage



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

    # main_page.click_on_register()

    # register_link_page = RegisterLinkPage(driver)
    # register_link_page.registration_with_dataset()

    main_page.click_on_login()

    login_link_page = LoginLinkPage(driver)
    login_link_page.user_authorization()
