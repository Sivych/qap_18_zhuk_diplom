from selenium.webdriver.common.by import By


class MenuElectronicsLocators:
    CAMERA_PHOTO_SECTION = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]/div/h2/a')
    CELL_PHONES_SECTION = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[2]/div/h2/a')

    PHONES_SMARTPHONE = (By.XPATH, '//img[@alt="Picture of Smartphone"]')
    PHONES_SMARTPHONE_CART_NAME = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody')
    PHONES_PHONE_COVER = (By.XPATH, '//img[@alt="Picture of Phone Cover"]')

    MANUFACTURER_DROPDOWN_MENU = (By.CSS_SELECTOR, 'select[id="product_attribute_80_2_37"]')
    MANUFACTURER_LIST = (By.CSS_SELECTOR, 'select[id="product_attribute_80_2_37"] option[value]')
    COLOR_DROPDOWN_MENU = (By.CSS_SELECTOR, 'select[id="product_attribute_80_1_38"]')
    COLOR_LIST = (By.CSS_SELECTOR, 'select[id="product_attribute_80_1_38"] option[value]')

    QUANTITY_FIELD = (By.CSS_SELECTOR, 'input[class="qty-input"]')
    ADD_TO_CART_BUTTON_PHONE_COVER = (By.CSS_SELECTOR, 'input[id="add-to-cart-button-80"]')
    ADD_TO_CART_BUTTON_SMARTPHONE = (By.CSS_SELECTOR, 'input[id="add-to-cart-button-43"]')

