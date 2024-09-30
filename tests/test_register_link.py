import allure
from pages import MainPage
from pages.register_link_page import RegisterLinkPage


@allure.feature("Header Links")
@allure.title("Open register link")
def test_open_register_link(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.assert_register_page_is_opened()


@allure.feature("Header Links")
@allure.title("Registration without entering data")
def test_registration_without_entering_data(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    main_page.click_on_register_button()
    register_link_page.validation_message()


@allure.feature("Header Links")
@allure.title("Random new user input data")
def test_random_new_user_input_data(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.randon_new_user_input_data()


@allure.feature("Header Links")
@allure.title("Empty email field")
def test_empty_email_field(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.empty_email_field()


@allure.feature("Header Links")
@allure.title("Email in lowercase")
def test_email_in_lowercase(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_in_lowercase()


@allure.feature("Header Links")
@allure.title("Email in uppercase")
def test_email_in_uppercase(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_in_uppercase()


@allure.feature("Header Links")
@allure.title("Email with numbers in the account name")
def test_email_with_numbers(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_with_numbers()


@allure.feature("Header Links")
@allure.title("Email with numbers in the domain part")
def test_email_with_numbers_in_domain(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_with_numbers_in_domain()


@allure.feature("Header Links")
@allure.title("Email with a hyphen in the account name")
def test_email_with_hyphen(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_with_hyphen()


@allure.feature("Header Links")
@allure.title("Email with a hyphen in the domain part")
def test_email_with_hyphen_in_domain(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_with_hyphen_in_domain()


@allure.feature("Header Links")
@allure.title("Email with underscore in account name")
def test_email_with_underscore(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_with_underscore()


@allure.feature("Header Links")
@allure.title("Email with underscore in the domain part")
def test_email_with_underscore_in_domain(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_with_underscore_in_domain()


@allure.feature("Header Links")
@allure.title("Email with dots in account name")
def test_email_with_dots(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_with_dots()


@allure.feature("Header Links")
@allure.title("Email with multiple dots in the domain part")
def test_email_with_dots_in_domain(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_with_dots_in_domain()


@allure.feature("Header Links")
@allure.title("Email without points in the domain part")
def test_email_without_points_in_domain(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_without_points_in_domain()


@allure.feature("Header Links")
@allure.title("Email exceeding the length (> 320 characters")
def test_email_exceeding_the_length(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_exceeding_the_length()


@allure.feature("Header Links")
@allure.title("Lack @ in email")
def test_lack_commercial_at_in_email(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.lack_commercial_at_in_email()


@allure.feature("Header Links")
@allure.title("Email with spaces in the name of the account")
def test_email_with_spaces(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_with_spaces()


@allure.feature("Header Links")
@allure.title("Email with spaces in the domain part")
def test_email_with_spaces_in_domain(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_with_spaces_in_domain()


@allure.feature("Header Links")
@allure.title("Email without an account")
def test_email_without_an_account(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_without_an_account()


@allure.feature("Header Links")
@allure.title("Email without domain")
def test_email_without_domain(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_register()

    register_link_page = RegisterLinkPage(driver)
    register_link_page.email_without_domain()