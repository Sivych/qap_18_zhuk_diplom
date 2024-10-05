from selenium.webdriver.common.by import By


class MenuBooksLocators:
    BOOK_COMPUTING_AND_INTERNET_ADD_TO_CART = (By.XPATH,
                                               '/html/body/div[4]/div[1]/div[4]/div[2]/'
                                               'div[2]/div[2]/div[3]/div[1]/div/div[2]/div[3]/div[2]/input')
    BOOK_FICTION_ADD_TO_CART = (By.XPATH,
                                '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]'
                                '/div[3]/div[3]/div/div[2]/div[3]/div[2]/input')