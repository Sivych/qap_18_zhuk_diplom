from selenium.webdriver.common.by import By


class HeaderLinksLocators:
    REGISTER_MENU_BUTTON = (By.CSS_SELECTOR, '[class ="ico-register"]')
    SHOPPING_CART_MENU_BUTTON = (By.CSS_SELECTOR, '[id = "topcartlink"]')
    LOGIN_MENU_BUTTON = (By.CSS_SELECTOR, '[class="ico-login"]')
    WISHLIST_MENU_BUTTON = (By.CSS_SELECTOR, '[href = "/wishlist"]')

    REGISTER_BUTTON = (By.CSS_SELECTOR, 'input[id="register-button"]')

    # TEXT_SHOPPING_CART= '[class ="page-title"]'
    # CONTINUE_SHOPPING = '[class ="button-2 continue-shopping-button"]'
    # TABLE = '[class="cart"]'