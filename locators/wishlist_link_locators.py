from selenium.webdriver.common.by import By


class WishlistLinkLocators:
    WISHLIST_UPPER_MENU = (By.CSS_SELECTOR, 'span[class="wishlist-qty"]')
    REMOVE_FROM_WISHLIST_CHECKBOX = (By.CSS_SELECTOR, 'td[class="remove-from-cart"]')
    ADD_TO_CART_FROM_WISHLIST_CHECKBOX = (By.CSS_SELECTOR, 'input[name="addtocart"]')
    UPDATE_WISHLIST = (By.CSS_SELECTOR, 'input[name="updatecart"]')
    ADD_TO_CART_FROM_WISHLIST_BUTTON = (By.CSS_SELECTOR, 'input[name="addtocartbutton"]')
    EMPTY_WISH_LIST_TEXT = (By.CSS_SELECTOR, 'div[class="wishlist-content"]')
