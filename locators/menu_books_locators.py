from selenium.webdriver.common.by import By


class MenuBooksLocators:
    BOOK_COMPUTING_AND_INTERNET_ADD_TO_CART = (By.XPATH,
                                               '/html/body/div[4]/div[1]/div[4]/div[2]/'
                                               'div[2]/div[2]/div[3]/div[1]/div/div[2]/div[3]/div[2]/input')
    BOOK_FICTION_ADD_TO_CART = (By.XPATH,
                                '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]'
                                '/div[3]/div[3]/div/div[2]/div[3]/div[2]/input')

    REMOVE_FROM_CART_BOOK_COMPUTING_AND_INTERNET = (By.XPATH , '/html/body/div[4]/div[1]'
                                                               '/div[4]/div/div/div[2]/div/'
                                                               'form/table/tbody/tr[1]/td[1]/input')
    REMOVE_FROM_CART_BOOK_FICTION = (By.XPATH , '/html/body/div[4]/div[1]'
                                                '/div[4]/div/div/div[2]/div/'
                                                'form/table/tbody/tr[2]/td[1]/input')