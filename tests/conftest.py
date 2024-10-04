import os
import pytest
import sys


from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

sys.path.append(os.path.abspath(''))


def pytest_addoption(parser):
    parser.addoption(
        "--firefox", action="store_true", default=False, help="Run tests in Firefox"
    )


@pytest.fixture
def driver(request):
    if request.config.getoption("--firefox"):
        options = webdriver.FirefoxOptions()
        gecko_install = GeckoDriverManager().install()
        folder = os.path.dirname(gecko_install)
        geckodriver_path = os.path.join(folder, "geckodriver.exe")
        service = FirefoxService(geckodriver_path)
        driver = webdriver.Firefox(service=service, options=options)
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-search-engine-choice-screen")
        chrome_install = ChromeDriverManager().install()
        folder = os.path.dirname(chrome_install)
        chromedriver_path = os.path.join(folder, "chromedriver.exe")
        service = ChromeService(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    yield driver

    driver.quit()


# import os
#
# import pytest
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @pytest.fixture
# def driver():
#     options = Options()
# #    options.add_argument('--window-size=1920,1080')
#     options.add_argument("--disable-search-engine-choice-screen")
#     chrome_install = ChromeDriverManager().install()
#     folder = os.path.dirname(chrome_install)
#     chromedriver_path = os.path.join(folder, "chromedriver.exe")
#     chrome_service = Service(chromedriver_path)
#     driver = webdriver.Chrome(service=chrome_service, options=options)
#     driver.maximize_window()
#     yield driver
#
#     driver.quit()
#     driver.close()
