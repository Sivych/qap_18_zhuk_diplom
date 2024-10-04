PYTEST=pytest
ALLURE_DIR=allure-results
ALL=allure_all
LOGIN_LINK=allure_login_link
MAIN=allure_main
MENU_BOOKS=allure_menu_books
MENU_COMPUTERS=allure_menu_computers
MENU_ELECTRONICS=allure_menu_electronics
REGISTER_LINK=allure_register_link
SHOPPING_CART_LINK=allure_shopping_cart_link
WISHLIST_LINK=allure_wishlist_link

LOGIN_LINK_FILES = tests/test_login_link.py
MAIN_FILES = tests/test_main.py
MENU_ELECTRONICS_FILES = tests/test_menu_electronics.py
HEADER_MENU_FILES = tests/test_open_header_menu.py
REGISTER_LINK_FILES = tests/test_register_link.py
SHOPPING_CART_LINK_FILES = tests/test_shopping_cart_link.py
WISHLIST_LINK_FILES = tests/test_wishlist_link.py

test-all:
	@echo Run all tests with chrome
	$(PYTEST) --alluredir $(ALLURE_DIR) $(ALL) --clean-alluredir

test-all-firefox:
	@echo Run all tests with firefox
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR) $(ALL) --clean-alluredir

test-login_link:
	@echo Run all tests login link page with chrome
	$(PYTEST) --alluredir $(ALLURE_DIR) $(LOGIN_LINK) $(LOGIN_LINK_FILES)

test-login_link-firefox:
	@echo Run all tests login link page with firefox
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR) $(LOGIN_LINK) $(LOGIN_LINK_FILES)

test-main:
	@echo Run all tests main page with chrome
	$(PYTEST) --alluredir $(ALLURE_DIR) $(MAIN) $(MAIN_FILES)

test-main-firefox:
	@echo Run all tests main page with firefox
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR) $(MAIN) $(MAIN_FILES)

test-electronics:
	@echo Run all tests menu electronics page with chrome
	$(PYTEST) --alluredir $(ALLURE_DIR) $(MENU_ELECTRONICS) $(MENU_ELECTRONICS_FILES)

test-electronics-firefox:
	@echo Run all tests menu electronics page with firefox
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR) $(MENU_ELECTRONICS) $(MENU_ELECTRONICS_FILES)

test-header:
	@echo Run all tests open header menu with chrome
	$(PYTEST) --alluredir $(ALLURE_DIR) $(HEADER_MENU_FILES)

test-electronics-firefox:
	@echo Run all tests open header menu with firefox
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR) $(HEADER_MENU_FILES)

test-register_link:
	@echo Run all tests register link page with chrome
	$(PYTEST) --alluredir $(ALLURE_DIR) $(REGISTER_LINK) $(REGISTER_LINK_FILES)

test-register_link-firefox:
	@echo Run all tests register link page with firefox
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR) $(REGISTER_LINK) $(REGISTER_LINK_FILES)

test-shopping_cart_link:
	@echo Run all tests shopping cart link page with chrome
	$(PYTEST) --alluredir $(ALLURE_DIR) $(SHOPPING_CART_LINK) $(SHOPPING_CART_LINK_FILES)

test-shopping_cart_link-firefox:
	@echo Run all tests shopping cart link page with firefox
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR) $(SHOPPING_CART_LINK) $(SHOPPING_CART_LINK_FILES)

test-wishlist_link:
	@echo Run all tests wishlist link page with chrome
	$(PYTEST) --alluredir $(ALLURE_DIR) $(WISHLIST_LINK) $(WISHLIST_LINK_FILES)

test-wishlist_link-firefox:
	@echo Run all tests wishlist link page with firefox
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR) $(WISHLIST_LINK) $(WISHLIST_LINK_FILES)


report-all:
	allure serve $(ALLURE_DIR) $(ALL)

report-login_link:
	allure serve $(ALLURE_DIR)$(LOGIN_LINK)

report-main:
	allure serve $(ALLURE_DIR)$(MAIN)

report-menu_books:
	allure serve $(ALLURE_DIR)$(MENU_BOOKS)

report-menu_computers:
	allure serve $(ALLURE_DIR)$(MENU_COMPUTERS)

report-menu_electronics:
	allure serve $(ALLURE_DIR)$(MENU_ELECTRONICS)

report-register_link:
	allure serve $(ALLURE_DIR)$(REGISTER_LINK)

report-shopping_cart_link:
	allure serve $(ALLURE_DIR)$(SHOPPING_CART_LINK)

report-wishlist_link:
	allure serve $(ALLURE_DIR)$(WISHLIST_LINK)

clean:
	@echo Clean all allure reports
	allure generate --clean --output $(ALLURE_DIR)






