from selenium.webdriver.common.by import By


class LoginLinkLocators:
    VALIDATION_SUMMARY_ERRORS = (By.CSS_SELECTOR, '[class ="validation-summary-errors"]')
    YOUR_PERSONAL_DETAILS_TEXT = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]'
                                            '/div/div[2]/form/div[2]/div[1]/strong')
    ACCOUNT_LINKS = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a')
    PERSONAL_DETAILS_FIRST_NAME = (By.XPATH, '//*[@id="FirstName"]')
    PERSONAL_DETAILS_LAST_NAME = (By.XPATH, '//*[@id="LastName"]')
    CHANGE_PASSWORD_BLOCK = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[1]/div/div[2]/ul/li[7]/a')
    INTRODUCTION_OLD_PASSWORD = (By.XPATH, '//*[@id="OldPassword"]')
    INTRODUCTION_NEW_PASSWORD = (By.XPATH, '//*[@id="NewPassword"]')
    INTRODUCTION_CONFIRM_NEW_PASSWORD = (By.XPATH, '//*[@id="ConfirmNewPassword"]')
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.change-password-button')
    CHANGE_PASSWORD_MASSAGE = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[2]')
    ERROR_CHANGE_PASSWORD_MASSAGE = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/form/div/div[2]/div[1]/div/ul/li')
    ACCOUNT_LOGIN_WINDOW = (By.CSS_SELECTOR, '[class="returning-wrapper"]')