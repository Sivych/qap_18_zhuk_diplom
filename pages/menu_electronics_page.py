import time

import allure

import random
from elements import HeaderMenu, HeaderLinks
from helpers.urls import MENU_ELECTRONICS
from locators import MainLocators, MenuElectronicsLocators
from pages import BasePage
from selenium.webdriver.support.ui import Select


class MenuElectronicsPage(MenuElectronicsLocators, HeaderLinks, MainLocators, HeaderMenu, BasePage):
    def init(self, driver):
        super().__init__(driver)

    @allure.step("Open menu ELECTRONICS")
    def open_menu_electronics(self):
        self.open_page(MENU_ELECTRONICS)

    @allure.step("Checking the opening of the menu electronics")
    def assert_that_menu_electronics_is_opened(self):
        self.assertions.assert_that_element_containce_text(self.TEXT_PAGE_TITLE, 'Electronics')
        assert self.get_element(self.CAMERA_PHOTO_SECTION)
        assert self.get_element(self.CELL_PHONES_SECTION)
        assert self.get_element(self.PAGE_BODY)
        assert self.get_element(self.FOOTER_MENU_WRAPPER)
        self.save_screenshot('menu_electronics_is_opened.png')

    @allure.step("Check phone cover options")
    def check_phone_cover_options(self):
        """Проверка работы параметров телефона Phone Cover"""
        self.click(self.CELL_PHONES_SECTION)
        self.click(self.PHONES_PHONE_COVER)
        self.click(self.MANUFACTURER_DROPDOWN_MENU)
        manufacturers = self.get_elements(self.MANUFACTURER_LIST)
        available_manufacturers_list = []
        for title in manufacturers:
            manufacturer_title = title.text
            available_manufacturers_list.append(manufacturer_title)
        assert len(available_manufacturers_list) == 2
        self.click(self.COLOR_DROPDOWN_MENU)
        colors = self.get_elements(self.COLOR_LIST)
        available_colors_list = []
        for color in colors:
            color_title = color.text
            available_colors_list.append(color_title)
        assert available_colors_list == ['Black', 'White', 'Blue', 'Yellow']

    @allure.step("Adding a Phone Cover to the cart with a positive quantity")
    def add_phone_cover_to_cart(self):
        """Добавление телефона Phone Cover в корзину с вводом позитивного количества"""
        self.click(self.CELL_PHONES_SECTION)
        self.click(self.PHONES_PHONE_COVER)
        self.click(self.MANUFACTURER_DROPDOWN_MENU)
        manufacturers = self.get_elements(self.MANUFACTURER_LIST)
        available_manufacturers_list = []
        for title in manufacturers:
            manufacturer_title = title.text
            available_manufacturers_list.append(manufacturer_title)
        Select(self.get_element(self.MANUFACTURER_DROPDOWN_MENU)).select_by_index(
            random.randint(0, len(available_manufacturers_list) - 1))
        self.click(self.COLOR_DROPDOWN_MENU)
        colors = self.get_elements(self.COLOR_LIST)
        available_colors_list = []
        for color in colors:
            color_title = color.text
            available_colors_list.append(color_title)
        Select(self.get_element(self.COLOR_DROPDOWN_MENU)).select_by_index(
            random.randint(0, len(available_colors_list) - 1))
        self.clear(self.QUANTITY_FIELD)
        positive_values = ['1', '10000', '2', '9999', '32']
        self.fill(self.QUANTITY_FIELD, random.choice(positive_values))
        self.click(self.ADD_TO_CART_BUTTON_PHONE_COVER)

    @allure.step("Checking if Phone Cover is in Cart")
    def checking_if_phone_cover_is_in_cart(self):
        """Проверка наличия в корзине телефона Phone Cover"""
        assert self.get_element(self.PHONES_SMARTPHONE_CART_NAME)

    @allure.step("Adding a Smartphone to the cart with a negative qty values")
    def add_negative_qty_values_smartphone(self):
        """Добавление телефона Smartphone в корзину с вводом негативного количества"""
        self.click(self.CELL_PHONES_SECTION)
        self.click(self.PHONES_SMARTPHONE)
        self.click(self.QUANTITY_FIELD)
        self.clear(self.QUANTITY_FIELD)
        negative_values = ['-1', '0', '-10000', 'ten', 'overninethousands']
        self.fill(self.QUANTITY_FIELD, random.choice(negative_values))
        self.click(self.ADD_TO_CART_BUTTON_SMARTPHONE)

    @allure.step("Check for negative quantity input")
    def check_for_negative_quantity_input(self):
        """Проверка на ввод негативного количества товара"""
        self.assertions.assert_that_element_containce_text(self.CART_WARNING_TEXT,
                                                           'Quantity should be positive')

    @allure.step("Adding a Smartphone to the cart over limit values")
    def add_over_limit_qty_values_smartphone(self):
        """Добавление телефона Smartphone в корзину с вводом более максимально допустимого количества"""
        self.click(self.CELL_PHONES_SECTION)
        self.click(self.PHONES_SMARTPHONE)
        self.click(self.QUANTITY_FIELD)
        self.clear(self.QUANTITY_FIELD)
        exceeded_values = ['10001', '20000', '30000']
        self.fill(self.QUANTITY_FIELD, random.choice(exceeded_values))
        self.click(self.ADD_TO_CART_BUTTON_SMARTPHONE)

    @allure.step("Checking for limit values input")
    def checking_for_limit_values_input(self):
        """Проверка на ввод запредельных значений количества товара"""
        self.assertions.assert_that_element_containce_text(self.CART_WARNING_TEXT,
                                                           'The maximum quantity allowed for purchase is 10000.')