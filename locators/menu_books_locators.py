from selenium.webdriver.common.by import By


class MenuBooksLocators:
    TEXT_SORT_BY = (By.CLASS_NAME, 'product-sorting')
    SORT_BY = (By.CSS_SELECTOR, '[id="products-orderby"]')
    ADD_TO_CART_IN_THE_WINDOW = (By.CSS_SELECTOR, '[class="button-2 product-box-add-to-cart-button"]:only-child')
    ADD_TO_CART_IN_PRODUCT_CART = (By.CSS_SELECTOR, '[class="button-1 add-to-cart-button"]')

    BOOK_COMPUTING_AND_INTERNET = (By.XPATH, '[//img[@alt="Picture of Computing and Internet"]')
    BOOK_COPY_OF_COMPUTING_AND_INTERNET_EX = (By.XPATH, '[//img[@alt="Picture of Copy of Computing and Internet EX"]')
    BOOK_FICTION = (By.XPATH, '[//img[@alt="Picture of Fiction"]')
    BOOK_FICTION_EX = (By.XPATH, '[//img[@alt="Picture of Fiction EX"]')
    BOOK_HEALTH = (By.XPATH, '[//img[@alt="Picture of Health Book"]')
    BOOK_SCIENCE = (By.XPATH, '[//img[@alt="Picture of Science"]')
