from selenium.webdriver.common.by import By


class MenuComputersLocators:
   PAGE_BODY = (By.CLASS_NAME, 'page-body')

   # CATEGORY_DESKTOPS_PICTURE = (By.XPATH, '//img[@alt="Picture for category Desktops"]')
   # CATEGORY_NOTEBOOKS_PICTURE = (By.XPATH, '//img[@alt="Picture for category Notebooks"]')
   # CATEGORY_ACCESSORIES_PICTURE = (By.XPATH, '//img[@alt="Picture for category Accessories"]')

   TCP_COACHING_DAY_ADD_TO_CART = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]'
                                             '/div[2]/div[2]/div[3]/div[1]/div/div[2]/div[3]/div[2]/input')
   TCP_INSTRUCTOR_LED_TRAINING = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]'
                                             '/div[2]/div[3]/div[2]/div/div[2]/div[3]/div[2]/input')
