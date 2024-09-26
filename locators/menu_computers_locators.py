from selenium.webdriver.common.by import By


class MenuComputersLocators:
   TEXT_SORT_BY = (By.CLASS_NAME, 'product-sorting')
   SORT_BY = (By.CSS_SELECTOR, '[id="products-orderby"]')
   PAGE_BODY = (By.CLASS_NAME, 'page-body')
   CATEGORY_DESKTOPS_PICTURE = (By.XPATH, '//img[@alt="Picture for category Desktops"]')
   CATEGORY_NOTEBOOKS_PICTURE = (By.XPATH, '//img[@alt="Picture for category Notebooks"]')
   CATEGORY_ACCESSORIES_PICTURE = (By.XPATH, '//img[@alt="Picture for category Accessories"]')

   BUILD_YOUR_OWN_CHEAP_COMPUTER = (By.XPATH, '//img[@alt="Picture of Build your own cheap computer"]')
   BUILD_YOUR_OWN_COMPUTER = (By.XPATH, '//img[@alt="Picture of Build your own computer"]')
   BUILD_YOUR_OWN_EXPENSIVE_COMPUTER = (By.XPATH, '//img[@alt="Picture of Build your own expensive  computer"]')
   DESKTOP_PC_WITH_CDRW = (By.XPATH, '//img[@alt="Picture of Desktop PC with CDRW""]')
   ELITE_DESKTOP_PC = (By.XPATH, '//img[@alt="Picture of Elite Desktop PC"]')
   SIMPLE_COMPUTER = (By.XPATH, '//img[@alt="Picture of Simple Computer"]')

   NOTEBOOK_LAPTOP = (By.XPATH, '//img[@alt="Picture of 14.1-inch Laptop"]')

   TCP_COACHING_DAY_ADD_TO_CART = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]'
                                             '/div[2]/div[2]/div[3]/div[1]/div/div[2]/div[3]/div[2]/input')
   TCP_INSTRUCTOR_LED_TRAINING = (By.XPATH, '/html/body/div[4]/div[1]/div[4]/div[2]/div[2]'
                                             '/div[2]/div[3]/div[2]/div/div[2]/div[3]/div[2]/input')
