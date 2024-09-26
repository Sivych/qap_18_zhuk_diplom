from selenium.webdriver.common.by import By


class MenuApparelShoesLocators:
    APPAREL_TOP_ITEM_PAGE = (By.XPATH,
                             '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/h2/a')
    ITEM_NAME = (By.CSS_SELECTOR, 'h1[itemprop="name"]')
    APPAREL_TOP_ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, 'input[id="add-to-wishlist-button-5"]')
    ITEM_POLKA_TOP_WISHLIST_NAME = (By.XPATH,
                                    '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div[1]/form/table/tbody/tr/td[4]/a')
    ITEM_POLKA_TOP_CART_NAME = (By.XPATH,
                                '/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr/td[3]/a')


