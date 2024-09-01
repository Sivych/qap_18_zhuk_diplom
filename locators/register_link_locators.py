from selenium.webdriver.common.by import By


class RegisterLinkLocators:
    GENDER_LIST = (By.CSS_SELECTOR, 'label[class="forcheckbox"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="FirstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="LastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="Email"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[id="Password"]')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, 'input[id="ConfirmPassword"]')
    COMPLETED_REGISTRATION_TEXT = (By.CSS_SELECTOR, 'div[class="result"]')

    FIRST_NAME_OUTPUT = (By.CSS_SELECTOR, 'input#FirstName.text-box.single-line.valid')
    LAST_NAME_OUTPUT = (By.CSS_SELECTOR, 'input#LastName.text-box.single-line.valid')
    EMAIL_OUTPUT = (By.CSS_SELECTOR, 'input#Email.text-box.single-line.valid')

    VALIDATION_MESSAGE_TEXT = (By.CSS_SELECTOR, 'span[class="field-validation-error"]')
    FIRST_NAME_VALIDATION_ERROR = (By.CSS_SELECTOR, 'span[for="FirstName"]')
    LAST_NAME_VALIDATION_ERROR = (By.CSS_SELECTOR, 'span[for="LastName"]')
    EMAIL_VALIDATION_ERROR = (By.CSS_SELECTOR, 'span[for="Email"]')
    PASSWORD_VALIDATION_ERROR = (By.CSS_SELECTOR, 'span[for="Password"]')
    CONFIRM_PASSWORD_VALIDATION_ERROR = (By.CSS_SELECTOR, 'span[for="ConfirmPassword"]')




