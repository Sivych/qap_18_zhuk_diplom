import allure
import pytest
from pages import MainPage
from pages.register_link_page import RegisterLinkPage


@allure.feature("Header link Register")
class TestsHeaderLinkRegister:
    @allure.title("Open register link")
    def test_open_register_link(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_register()

        register_link_page = RegisterLinkPage(driver)
        register_link_page.assert_register_page_is_opened()

    @allure.title("Registration without entering data")
    def test_registration_without_entering_data(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_register()

        register_link_page = RegisterLinkPage(driver)
        register_link_page.validation_message()

    @allure.title("Random new user input data")
    def test_random_new_user_input_data(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_register()

        register_link_page = RegisterLinkPage(driver)
        register_link_page.randon_new_user_input_data()

    @allure.title("Empty email field")
    def test_empty_email_field(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_register()

        register_link_page = RegisterLinkPage(driver)
        register_link_page.empty_email_field()

    @pytest.mark.parametrize("successful_email", [str('asfgrwqet@mail.ru'), str('PETROVA@mail.ru'),
                                                  str('123456789@mail.ru'), str('Petrova-Alina@1234.com'),
                                                  str('Petrova_Alina@mail.com'), str('Petrova.Alina@mail.com')])
    @allure.title("Successful checking email name for validity: "
                  "email in lowercase, uppercase, "
                  "with numbers, with a hyphen, "
                  "with underscore, with dots,"
                  "email length exceeded (>320 characters)")
    def test_successful_check_email_name_for_valid(self, driver, successful_email):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_register()

        register_link_page = RegisterLinkPage(driver)
        register_link_page.check_email_name_for_validity(successful_email)

    @pytest.mark.parametrize("successful_email_domain", [str('PETROVA@1234.com'),
                                                         str('Petrova-Alina@strange-example.com'),
                                                         str('PetrovaAlina@strange_example.com'),
                                                         str('Petrova.Alina@strange.example.com')])
    @allure.title("Successful checked the validity of the email domain part: "
                  "with numbers, with hyphen,"
                  "with underscore, with dots")
    def test_check_valid_email_in_domain(self, driver, successful_email_domain):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_register()

        register_link_page = RegisterLinkPage(driver)
        register_link_page.check_valid_email_in_domain(successful_email_domain)

    @allure.title("Validation check Email exceeding the length (> 320 characters)")
    def test_valid_email_exceeding_the_length(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_register()

        register_link_page = RegisterLinkPage(driver)
        register_link_page.check_valid_email_exceeding_the_length()

    @pytest.mark.parametrize("invalid_email", [str('Petrova.Alina@strange_examplecom'),
                                               str('Petrova.Alina.strange_example.com'),
                                               str('Petrova Alina@strange_example.com'),
                                               str('PetrovaAlina@strange example.com'),
                                               str('@gmail.com'),
                                               str('Petrova_Alina')])
    @allure.title("Сheck for invalid email impassability:"
                  "email without points in domain,"
                  "Lack @ in email, with spaces Email name,"
                  "with spaces in the domain, Email without an account,"
                  "Email without domain")
    def test_lack_commercial_at_in_email(self, driver, invalid_email):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_register()

        register_link_page = RegisterLinkPage(driver)
        register_link_page.check_invalid_email_impassability(invalid_email)
