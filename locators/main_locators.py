from selenium.webdriver.common.by import By


class MainLocators:
    HEADER_LOGO = (By.CSS_SELECTOR, '[alt="Tricentis Demo Web Shop"]')
    HEADER_MENU = (By.CSS_SELECTOR, '[class="header-menu"]')
    SLIDER = (By.CSS_SELECTOR, '[class="nivoSlider"]')
    FOOTER_MENU_WRAPPER = (By.CLASS_NAME, 'footer-menu-wrapper')
    TEXT_PAGE_TITLE = (By.CLASS_NAME, 'page-title')