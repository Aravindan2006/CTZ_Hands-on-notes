from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def build_chrome_driver(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_size(1280, 800)
    return driver
