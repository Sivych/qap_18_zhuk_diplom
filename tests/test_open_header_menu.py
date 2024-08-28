from pages import MainPage
from pages.menu_books_page import MenuBooksPage


def test_open_menu_books(driver):
    main_page = MainPage(driver)

    main_page.open()
    main_page.assert_that_main_is_opened()

    main_page.click_on_menu_books()
    books_menu_page = MenuBooksPage(driver)
    books_menu_page.assert_that_menu_books_is_opened()