import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

SCREENSHOTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")


@pytest.fixture(scope="session")
def base_url():
    return "https://www.testmuai.com/selenium-playground/"


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.set_window_size(1280, 800)
    yield chrome_driver
    chrome_driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        chrome_driver = item.funcargs.get("driver")
        if chrome_driver:
            os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
            chrome_driver.save_screenshot(os.path.join(SCREENSHOTS_DIR, f"{item.name}_failure.png"))
