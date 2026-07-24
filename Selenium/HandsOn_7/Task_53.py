"""Task 53 - CheckboxPage."""

from pages.checkbox_page import CheckboxPage
from utils.helpers import build_chrome_driver

if __name__ == "__main__":
    driver = build_chrome_driver()
    try:
        page = CheckboxPage(driver)
        page.open()
        page.check_option(1)
        assert page.is_option_checked(1)
        page.uncheck_option(1)
        assert not page.is_option_checked(1)
    finally:
        driver.quit()
