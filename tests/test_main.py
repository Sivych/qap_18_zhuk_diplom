import allure

from pages import MainPage
from pages.menu_apparel_shoes_page import MenuApparelShoesPage
from pages.menu_books_page import MenuBooksPage
from pages.menu_computers_page import MenuComputersPage
from pages.menu_digital_downloads_page import MenuDigitalDownloadsPage
from pages.menu_electronics_page import MenuElectronicsPage
from pages.menu_gift_cards_page import MenuGiftCardsPage
from pages.menu_jewelry_page import MenuJewelryPage


@allure.feature("Headers Menu")
class TestsOpeningHeadersMenu:
    @allure.title("Opening main page")
    def test_that_main_page_is_opened(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.assert_that_main_is_opened()

    @allure.title("Opening menu BOOKS")
    def test_that_menu_books_is_opened(self, driver):
        books_menu_page = MenuBooksPage(driver)
        books_menu_page.open_menu_books()
        books_menu_page.assert_that_menu_books_is_opened()

    @allure.title("Opening menu COMPUTER")
    def test_open_menu_computers(self, driver):
        computers_menu_page = MenuComputersPage(driver)
        computers_menu_page.open_menu_computers()
        computers_menu_page.assert_that_menu_computers_is_opened()

    @allure.title("Opening menu ELECTRONICS")
    def test_open_menu_electronics(self, driver):
        electronics_menu_page = MenuElectronicsPage(driver)
        electronics_menu_page.open_menu_electronics()
        electronics_menu_page.assert_that_menu_electronics_is_opened()

    @allure.title("Opening menu APPAREL & SHOES")
    def test_open_menu_apparel_shoes(self, driver):
        apparel_shoes_menu_page = MenuApparelShoesPage(driver)
        apparel_shoes_menu_page.open_menu_apparel_shoes()
        apparel_shoes_menu_page.assert_that_menu_apparel_shoes_is_opened()

    @allure.title("Opening menu DIGITAL DOWNLOADS")
    def test_open_menu_digital_downloads(self, driver):
        digital_downloads_menu_page = MenuDigitalDownloadsPage(driver)
        digital_downloads_menu_page.open_menu_digital_downloads()
        digital_downloads_menu_page.assert_that_menu_digital_downloads_is_opened()

    @allure.title("Opening menu JEWELRY")
    def test_open_menu_jewelry(self, driver):
        jewelry_menu_page = MenuJewelryPage(driver)
        jewelry_menu_page.open_menu_jewelry()
        jewelry_menu_page.assert_that_menu_jewelry_is_opened()

    @allure.title("Opening menu GIFT CARDS")
    def test_open_menu_gift_cards(self, driver):
        gift_cards_menu_page = MenuGiftCardsPage(driver)
        gift_cards_menu_page.open_menu_gift_cards()
        gift_cards_menu_page.assert_that_menu_gift_cards_is_opened()


