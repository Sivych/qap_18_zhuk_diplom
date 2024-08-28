from selenium.webdriver.common.by import By


class MenuBooksLocators:
    TEXT_SORT_BY = (By.CLASS_NAME, 'product-sorting')
    SORT_BY = (By.CSS_SELECTOR, '[id="products-orderby"]')


#class MenuComputersLocators:
#    TEXT_SORT_BY = (By.CLASS_NAME, 'product-sorting')
#    SORT_BY = (By.CSS_SELECTOR, '[id="products-orderby"]')
#    PAGE_BODY = (By.CLASS_NAME, 'page-body')
