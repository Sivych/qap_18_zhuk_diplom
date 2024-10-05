from selenium.webdriver.common.by import By


class RegisterLinkLocators:
    GENDER_LIST = (By.CSS_SELECTOR, 'label[class="forcheckbox"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="FirstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="LastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="Email"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[id="Password"]')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input[id="ConfirmPassword"]')

    COMPLETED_REGISTRATION_TEXT = (By.CSS_SELECTOR, 'div[class="result"]')
    FIELD_VALIDATION_ERROR_EMAIL = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]'
                                              '/form/div/div[2]/div[2]/div[2]/div[4]/span[2]')

    FIRST_NAME_VALIDATION_ERROR = (By.CSS_SELECTOR, 'span[for="FirstName"]')
    LAST_NAME_VALIDATION_ERROR = (By.CSS_SELECTOR, 'span[for="LastName"]')
    EMAIL_VALIDATION_ERROR = (By.CSS_SELECTOR, 'span[for="Email"]')
    PASSWORD_VALIDATION_ERROR = (By.CSS_SELECTOR, 'span[for="Password"]')
    CONFIRM_PASSWORD_VALIDATION_ERROR = (By.CSS_SELECTOR, 'span[for="ConfirmPassword"]')




