import allure

from pages import MainPage


@allure.feature("Main feature")
@allure.title("Test that main is opened")
def test_that_main_is_opened(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.assert_that_main_is_opened()


