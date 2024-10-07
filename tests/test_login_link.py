import allure
import time

from pages import MainPage
from pages.login_link_page import LoginLinkPage


@allure.feature("Header link Login")
class TestsHeaderLinkLogin:
    @allure.title("Opening login page")
    def test_open_login_link(self, driver):
        login_link_page = LoginLinkPage(driver)
        login_link_page.open_login_link()
        login_link_page.assert_login_page_is_opened()

    @allure.title("Checking login on the ready data")
    def test_checking_login_on_the_ready_data(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_login()

        login_link_page = LoginLinkPage(driver)
        login_link_page.login_to_ready_data()
        time.sleep(1)
        login_link_page.checking_login_on_the_ready_data()

    @allure.title("Login check on non-existent data")
    def test_login_check_non_existent_data(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_login()

        login_link_page = LoginLinkPage(driver)
        login_link_page.login_with_non_existent_data()
        time.sleep(1)
        login_link_page.login_check_non_existent_data()

    @allure.title("Account verification")
    def test_open_account_customer_info(self, driver):
        login_link_page = LoginLinkPage(driver)
        login_link_page.open_login_link()
        login_link_page.login_to_ready_data()
        login_link_page.assert_account_customer_info()

    @allure.title("Password change on the user page")
    def test_password_change_on_the_user_page(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_login()

        login_link_page = LoginLinkPage(driver)
        login_link_page.login_to_ready_data()
        login_link_page.password_change_on_the_user_page()
        time.sleep(1)
        login_link_page.check_for_successful_password_change()

    @allure.title("Change password on page: incorrect entry of old password")
    def test_incorrect_entry_of_old_password(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_on_login()

        login_link_page = LoginLinkPage(driver)
        login_link_page.login_to_ready_data()
        login_link_page.incorrect_entry_of_old_password()
        time.sleep(1)
        login_link_page.check_for_incorrect_entry_of_old_password()




