from selenium.webdriver.common.by import By


class HeaderLinksLocators:
    REGISTER_MENU_BUTTON = (By.CSS_SELECTOR, '[class ="ico-register"]')
    SHOPPING_CART_MENU_BUTTON = (By.CSS_SELECTOR, '[id = "topcartlink"]')
    LOGIN_MENU_BUTTON = (By.CSS_SELECTOR, '[class="ico-login"]')
    WISHLIST_MENU_BUTTON = (By.CSS_SELECTOR, '[href = "/wishlist"]')

    REGISTER_BUTTON = (By.CSS_SELECTOR, 'input[id="register-button"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="button-1 login-button"]')
