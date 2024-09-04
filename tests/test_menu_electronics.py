import allure
from pages import MainPage
from pages.menu_electronics_page import MenuElectronicsPage


@allure.feature("Header Menu")
@allure.title("Test check phone cover options")
def test_check_phone_cover_options(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_menu_electronics()

    electronics_menu_page = MenuElectronicsPage(driver)
    electronics_menu_page.check_phone_cover_options()


@allure.feature("Header Menu")
@allure.title("Test add phone cover to cart")
def test_add_phone_cover_to_cart(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_menu_electronics()

    electronics_menu_page = MenuElectronicsPage(driver)
    electronics_menu_page.add_phone_cover_to_cart()


@allure.feature("Header Menu")
@allure.title("Test add negative qty values")
def test_add_negative_qty_values(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_menu_electronics()

    electronics_menu_page = MenuElectronicsPage(driver)
    electronics_menu_page.add_negative_qty_values()


@allure.feature("Header Menu")
@allure.title("Test add over limit qty values")
def test_add_over_limit_qty_values(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.click_on_menu_electronics()

    electronics_menu_page = MenuElectronicsPage(driver)
    electronics_menu_page.add_over_limit_qty_values()