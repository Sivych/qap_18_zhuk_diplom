import allure

from elements import HeaderMenu
from helpers import BASE_URL
from locators import MainLocators , MenuElectronicsLocators
from pages import BasePage


class MenuElectronicsPage(MenuElectronicsLocators , MainLocators , HeaderMenu , BasePage):
    def init(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(BASE_URL)

    def assert_that_menu_electronics_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE , 'Electronics')
        assert self.get_element(self.CATEGORY_CAMERA_PHOTO_PICTURE)
        assert self.get_element(self.CATEGORY_CELL_PHONES)

    def check_phone_cover_options(self):
        self.CATEGORY_CELL_PHONES.self.click()
        self.PHONES_PHONE_COVER.click()
        self.MANUFACTURER_DROPDOWN_MENU.click()
        manufacturers = self.get_element(self.MANUFACTURER_LIST)
        available_manufacturers_list = []
        for title in manufacturers:
            manufacturer_title = title.text
            available_manufacturers_list.append(manufacturer_title)
        assert len(available_manufacturers_list) == 2
        self.COLOR_DROPDOWN_MENU.click()
        colors = self.get_element(self.COLOR_LIST)
        available_colors_list = []
        for color in colors:
            color_title = color.text
            available_colors_list.append(color_title)
        assert available_colors_list == ['Black', 'White', 'Blue', 'Yellow']