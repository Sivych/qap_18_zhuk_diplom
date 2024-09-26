from selenium.webdriver.common.by import By


class MenuElectronicsLocators:
    CAMERA_PHOTO_SECTION = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]/div/h2/a')
    CELL_PHONES_SECTION = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[2]/div/h2/a')

    CAMERA_HARD_DRIVE = (By.XPATH, '//img[@alt="Picture of 1MP 60GB Hard Drive Handycam Camcorder"]')
    CAMERA_CAMCORDER = (By.XPATH, '//img[@alt="Picture of Camcorder""]')
    CAMERA_DIGITAL_SLR = (By.XPATH, '//img[@alt="Picture of Digital SLR Camera 12.2 Mpixel""]')
    CAMERA_HIGH_DEFINITION_CAMCORDER = (By.XPATH, '//img[@alt="Picture of High Definition 3D Camcorder"]')

    PHONES_SMARTPHONE = (By.XPATH, '//img[@alt="Picture of Smartphone"]')
    PHONES_SMARTPHONE_CART_NAME = (By.CSS_SELECTOR, '[href="/phone-cover"]')
    PHONES_USED_PHONE = (By.XPATH, '//img[@alt="Picture of Used phone"]')
    PHONES_PHONE_COVER = (By.XPATH, '//img[@alt="Picture of Phone Cover"]')

    MANUFACTURER_DROPDOWN_MENU = (By.CSS_SELECTOR, 'select[id="product_attribute_80_2_37"]')
    MANUFACTURER_LIST = (By.CSS_SELECTOR, 'select[id="product_attribute_80_2_37"] option[value]')
    COLOR_DROPDOWN_MENU = (By.CSS_SELECTOR, 'select[id="product_attribute_80_1_38"]')
    COLOR_LIST = (By.CSS_SELECTOR, 'select[id="product_attribute_80_1_38"] option[value]')

    QUANTITY_FIELD = (By.CSS_SELECTOR, 'input[class="qty-input"]')
    ADD_TO_CART_BUTTON_PHONE_COVER = (By.CSS_SELECTOR, 'input[id="add-to-cart-button-80"]')
    ADD_TO_CART_BUTTON_SMARTPHONE = (By.CSS_SELECTOR, 'input[id="add-to-cart-button-43"]')

