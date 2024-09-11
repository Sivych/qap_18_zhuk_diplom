from selenium.webdriver.common.by import By


class MainLocators:
    HEADER_LOGO = (By.CSS_SELECTOR, '[alt="Tricentis Demo Web Shop"]')
    HEADER_MENU = (By.CSS_SELECTOR, '[class="header-menu"]')
    SLIDER = (By.CSS_SELECTOR, '[class="nivoSlider"]')
    FOOTER_MENU_WRAPPER = (By.CLASS_NAME, 'footer-menu-wrapper')
    TEXT_PAGE_TITLE = (By.CLASS_NAME, 'page-title')
    CART_WARNING_TEXT = (By.CSS_SELECTOR, 'p[class="content"]')
 #   CART_ERROR_TEXT = (By.CSS_SELECTOR,'[class ="close"]')

    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[id="small-searchterms"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    PRODUCTS_TITLES = (By.CSS_SELECTOR, 'h2[class="product-title"]')
    NO_RESULT_TEXT = (By.CSS_SELECTOR, 'strong[class="result"]')
    SORT_BY_BUTTON = (By.CSS_SELECTOR, 'select[id="products-orderby"]')
    SORTING_OPTION_LOW_TO_HIGH = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/desktops?orderby'
                                                   '=10"]')
    ACTUAL_PRICES = (By.CSS_SELECTOR, 'span[class="price actual-price"]')
    SORTING_OPTION_HIGH_TO_LOW = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/desktops?orderby'
                                                   '=11"]')
    SORTING_OPTION_A_TO_Z = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/desktops?orderby=5"]')
    SORTING_OPTION_Z_TO_A = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/desktops?orderby=6"]')
    FILTER_UNDER_1000 = (By.CSS_SELECTOR, 'a[href="https://demowebshop.tricentis.com/desktops?price=-1000"]')
    FILTER_1000_1200 = (By.CSS_SELECTOR, 'a[href="https://demowebshop.tricentis.com/desktops?price=1000-1200"]')
    FILTER_OVER_1200 = (By.CSS_SELECTOR, 'a[href="https://demowebshop.tricentis.com/desktops?price=1200-"]')
    DISPLAY_BUTTON = (By.CSS_SELECTOR, 'select[id="products-pagesize"]')
    DISPLAY_OPTION_4_PER_PAGE = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/apparel-shoes'
                                                  '?pagesize=4"]')
    DISPLAY_OPTION_8_PER_PAGE = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/apparel-shoes'
                                                  '?pagesize=8"]')
    DISPLAY_OPTION_12_PER_PAGE = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/apparel-shoes'
                                                   '?pagesize=12"]')
    VIEW_AS_BUTTON = (By.CSS_SELECTOR, 'select[id="products-viewmode"]')
    VIEW_MODE_GRID = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/jewelry?viewmode=grid"]')
    VIEW_MODE_LIST = (By.CSS_SELECTOR, 'option[value="https://demowebshop.tricentis.com/jewelry?viewmode=list"]')

