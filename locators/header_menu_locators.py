from selenium.webdriver.common.by import By


class HeaderMenuLocators:
    MENU_BOOKS = (By.XPATH, '//a[@href="/books"]')
    MENU_COMPUTERS = (By.XPATH, '//a[@href="/computers"]')
    MENU_ELECTRONICS = (By.XPATH, '//a[@href="/electronics"]')
    MENU_APPAREL_SHOES = (By.XPATH, '//a[@href="/apparel-shoes"]')
    MENU_DIGITAL_DOWNL = (By.XPATH, '//a[href="/digital-downloads"]')
    MENU_JEWELRY = (By.XPATH, '//a[@href="/jewelry"]')
    MENU_GIFT_CARDS = (By.XPATH, '//a[@href="/gift-cards"]')

