from selenium.webdriver.common.by import By


class ShoppingCartLinkLocators:
    TEXT_SHOPPING_CART = (By.CSS_SELECTOR, '[class ="page-title"]')
    CONTINUE_SHOPPING = (By.CLASS_NAME, 'button-2 continue-shopping-button')
    TABLE = (By.CSS_SELECTOR, '[class="cart"]')
    TEXT_BODY = (By.CSS_SELECTOR, '[class="page-body"]')  # 'Your Shopping Cart is empty!'
    CONTINUE_SHOPPING_BUTTON = '[class ="button-2 continue-shopping-button"]'