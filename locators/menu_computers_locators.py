from selenium.webdriver.common.by import By


class MenuComputersLocators:
    DESKTOPS_SECTION = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]/div')
    NOTEBOOKS_SECTION = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[2]/div')
    ACCESSORIES_SECTION = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[3]/div')

    TCP_COACHING_DAY_ADD_TO_CART = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]'
                                              '/div[2]/div[2]/div[3]/div[1]/div/div[2]'
                                              '/div[3]/div[2]/input')
    TCP_INSTRUCTOR_LED_TRAINING = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]'
                                             '/div[2]/div[3]/div[2]/div/div[2]/div[3]/div[2]/input')
