from selenium.webdriver.common.by import By


class CartLocators:
    TEXT_SHOPPING_CART = (By.CSS_SELECTOR, '[class ="page-title"]')
    CONTINUE_SHOPPING = (By.CLASS_NAME, 'button-2 continue-shopping-button')
    TABLE = (By.CSS_SELECTOR, '[class="cart"]')
    TEXT_BODY = (By.CSS_SELECTOR, '[class="page-body"]')