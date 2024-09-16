from selenium.webdriver.common.by import By


class LoginLinkLocators:
    TEXT_LOGIN = (By.CSS_SELECTOR, '[class="page-title"]')
    VALIDATION_SUMMARY_ERRORS = (By.CSS_SELECTOR, '[class ="validation-summary-errors"]')
