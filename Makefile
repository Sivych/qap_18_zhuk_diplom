test_head:
	@echo Run test
	pytest -m only --headless=yes --browser==chrome --reruns 5 -n 5

PYTEST=pytest
ALLURE_DIR=allure-results
ALL=allure_all
#API=allure_api
MAIN=allure_main
BASKET=allure_basket
DELIVERY=allure_delivery
LOGIN=allure_login

#PRODUCT=allure_product
#CONTACT=allure_contact

MAIN_FILES = tests/test_main.py
BASKET_FILES = tests/test_basket.py
DELIVERY_FILES = tests/test_delivery_page.py
LOGIN_FILES = tests/test_login_page.py

PRODUCT_FILES = tests/test_product.py
CONTACT_FILES = tests/test_contact_page.py

test-all:
	@echo Run all test
	$(PYTEST) #--alluredir $(ALLURE_DIR)$(ALL)

test-all-firefox:
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR)$(ALL)

test-basket:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(BASKET) $(BASKET_FILES)

test-delivery:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(DELIVERY) $(DELIVERY_FILES)

test-login:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(LOGIN) $(LOGIN_FILES)

test-main:
	@echo Run test
	$(PYTEST) -m only --headless=yes --alluredir $(MAIN_FILES)

test-product:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(PRODUCT) $(PRODUCT_FILES)

test-contact:
	$(PYTEST) --alluredir $(ALLURE_DIR)$(CONTACT) $(CONTACT_FILES)

#test-api-firefox:
#	$(PYTEST) --firefox --alluredir $(ALLURE_DIR)$(API) $(API_FILES)

test-basket-firefox:
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR)$(BASKET) $(BASKET_FILES)

test-delivery-firefox:
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR)$(DELIVERY) $(DELIVERY_FILES)

test-login-firefox:
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR)$(LOGIN) $(LOGIN_FILES)

test-main-firefox:
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR)$(MAIN) $(MAIN_FILES)

test-product-firefox:
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR)$(PRODUCT) $(PRODUCT_FILES)

test-contact-firefox:
	$(PYTEST) --firefox --alluredir $(ALLURE_DIR)$(CONTACT) $(CONTACT_FILES)

report-all:
	allure serve $(ALLURE_DIR)$(ALL)

#report-api:
#	allure serve $(ALLURE_DIR)$(API)

report-basket:
	allure serve $(ALLURE_DIR)$(BASKET)

report-delivery:
	allure serve $(ALLURE_DIR)$(DELIVERY)

report-login:
	allure serve $(ALLURE_DIR)$(LOGIN)

report-main:
	allure serve $(ALLURE_DIR)$(MAIN)

report-product:
	allure serve $(ALLURE_DIR)$(PRODUCT)

report-contact:
	allure serve $(ALLURE_DIR)$(CONTACT)

clean-allure:
	rm -rf allure-results/