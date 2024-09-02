from selenium.webdriver.common.by import By


class MenuApparelShoesLocators:
    APPAREL_TOP_ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, 'input[id="add-to-wishlist-button-5"]')
    WISHLIST_UPPER_MENU = (By.CSS_SELECTOR, 'span[class="wishlist-qty"]')
    REMOVE_FROM_WISHLIST_CHECKBOX = (By.CSS_SELECTOR, 'td[class="remove-from-cart"]')
    ADD_TO_CART_FROM_WISHLIST_CHECKBOX = (By.CSS_SELECTOR, 'input[name="addtocart"]')
    UPDATE_WISHLIST = (By.CSS_SELECTOR, 'input[name="updatecart"]')
    ADD_TO_CART_FROM_WISHLIST_BUTTON = (By.CSS_SELECTOR, 'input[name="addtocartbutton"]')
    EMPTY_WISH_LIST_TEXT = (By.CSS_SELECTOR, 'div[class="wishlist-content"]')
    ITEM_POLKA_TOP_WISHLIST_NAME = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div['
                                              '1]/form/table/tbody/tr/td[4]/a')
    ITEM_POLKA_TOP_CART_NAME = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/'
                                          'table/tbody/tr/td[3]/a')