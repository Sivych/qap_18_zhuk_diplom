from selenium.webdriver.common.by import By


class ShoppingCartLinkLocators:
    TEXT_SHOPPING_CART = (By.CSS_SELECTOR, '[class ="page-title"]')

    CONTINUE_SHOPPING = (By.CLASS_NAME, 'button-2 continue-shopping-button')
    TABLE = (By.CSS_SELECTOR, '[class="cart"]')
    CONTINUE_SHOPPING_BUTTON = '[class ="button-2 continue-shopping-button"]'
    UPDATE_SHOPPING_CART_BUTTON = (By.CSS_SELECTOR, '[class="button-2 update-cart-button"]')

    TERMS_OF_SERVICE = (By.XPATH, '//*[@id="termsofservice"]')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '[id="checkout"]')
    CHECKOUT_GUEST_OR_REGISTER_TEXT = (By.XPATH, '/html/body/div[4]/div[1]/div[4]'
                                                 '/div[2]/div/div[2]/div[1]/div[1]/div[1]/strong')

