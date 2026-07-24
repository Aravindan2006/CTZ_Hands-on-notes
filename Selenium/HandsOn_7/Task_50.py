"""Task 50 - BasePage: navigate_to, get_title, wait_for_element. Real implementation in pages/base_page.py."""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import BASE_URL
from utils.helpers import build_chrome_driver

if __name__ == "__main__":
    driver = build_chrome_driver()
    try:
        page = BasePage(driver)
        page.navigate_to(BASE_URL)
        print(page.get_title())
        print(page.wait_for_element((By.TAG_NAME, "h1")).text)
    finally:
        driver.quit()
