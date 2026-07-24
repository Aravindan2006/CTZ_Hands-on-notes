"""Task 51 - SimpleFormPage locators are class-level tuples, not hardcoded in methods."""

from pages.simple_form_page import SimpleFormPage
from utils.helpers import build_chrome_driver

if __name__ == "__main__":
    driver = build_chrome_driver()
    try:
        page = SimpleFormPage(driver)
        page.open()
        print(page.MESSAGE_INPUT, page.SUBMIT_BUTTON)
    finally:
        driver.quit()
