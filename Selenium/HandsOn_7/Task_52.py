"""Task 52 - SimpleFormPage interaction methods return values, don't assert."""

from pages.simple_form_page import SimpleFormPage
from utils.helpers import build_chrome_driver

if __name__ == "__main__":
    driver = build_chrome_driver()
    try:
        page = SimpleFormPage(driver)
        page.open()
        page.enter_message("Hello Selenium")
        page.click_submit()
        assert page.get_displayed_message() == "Hello Selenium"
    finally:
        driver.quit()
