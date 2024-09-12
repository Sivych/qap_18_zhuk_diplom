import allure
from pages import MainPage
from pages.menu_books_page import MenuBooksPage
from pages.menu_computers_page import MenuComputersPage
from pages.menu_electronics_page import MenuElectronicsPage


@allure.feature("Header Menu")
@allure.title("Open menu book")
def test_open_menu_books(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_menu_books()
    books_menu_page = MenuBooksPage(driver)
    books_menu_page.assert_that_menu_books_is_opened()


@allure.feature("Header Menu")
@allure.title("Open menu computers")
def test_open_menu_computers(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_menu_computers()
    computers_menu_page = MenuComputersPage(driver)
    computers_menu_page.assert_that_menu_computers_is_opened()


@allure.feature("Header Menu")
@allure.title("Open menu electronics")
def test_open_menu_electronics(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_menu_electronics()
    electronics_menu_page = MenuElectronicsPage(driver)
    electronics_menu_page.assert_that_menu_electronics_is_opened()







