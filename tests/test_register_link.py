import allure
from pages import MainPage
from pages.register_link_page import RegisterLinkPage


@allure.feature("Header Links")
@allure.title("Test open register link")
def test_open_register_link(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.assert_register_page_is_opened()


@allure.feature("Header Links")
@allure.title("Test registration without entering data")
def test_registration_without_entering_data(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.assert_register_page_is_opened()

    main_page.click_on_register_button()

    register_link_page.validation_message()


@allure.feature("Header Links")
@allure.title("Random new user input data")
def test_random_new_user_input_data(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.assert_register_page_is_opened()
    register_link_page.randon_new_user_input_data()


@allure.feature("Header Links")
@allure.title("Registration with dataset")
def test_registration_with_dataset(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.registration_with_dataset()