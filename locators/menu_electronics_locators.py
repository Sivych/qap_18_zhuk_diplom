from selenium.webdriver.common.by import By


class MenuElectronicsLocators:
    CATEGORY_CAMERA_PHOTO_PICTURE = (By.XPATH, '//img[@alt="Picture for category Camera, photo"]')
    CATEGORY_CELL_PHONES = (By.XPATH, '//img[@alt="Picture for category Cell phones"]')

    CAMERA_HARD_DRIVE = (By.XPATH, '//img[@alt="Picture of 1MP 60GB Hard Drive Handycam Camcorder"]')
    CAMERA_CAMCORDER = (By.XPATH, '//img[@alt="Picture of Camcorder""]')
    CAMERA_DIGITAL_SLR = (By.XPATH, '//img[@alt="Picture of Digital SLR Camera 12.2 Mpixel""]')
    CAMERA_HIGH_DEFINITION_CAMCORDER = (By.XPATH, '//img[@alt="Picture of High Definition 3D Camcorder"]')

    PHONES_SMARTPHONE = (By.XPATH, '//img[@alt="Picture of Smartphone"]')
    PHONES_USED_PHONE = (By.XPATH, '//img[@alt="Picture of Used phone"]')
    PHONES_PHONE_COVER = (By.XPATH, '//img[@alt="Picture of Phone Cover"]')