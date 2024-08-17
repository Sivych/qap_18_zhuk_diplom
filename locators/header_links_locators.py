from selenium.webdriver.common.by import By


class HeaderLinksLocators:
    REGISTER = (By.CSS_SELECTOR, '[class ="ico-register"]')
    SHOPPING_CART = (By.CSS_SELECTOR, '[id = "topcartlink"]')
    # TEXT_SHOPPING_CART= '[class ="page-title"]'
    # CONTINUE_SHOPPING = '[class ="button-2 continue-shopping-button"]'
    # TABLE = '[class="cart"]'