"""Task 54 - DropdownPage, uses Select internally."""

from pages.dropdown_page import DropdownPage
from utils.helpers import build_chrome_driver

if __name__ == "__main__":
    driver = build_chrome_driver()
    try:
        page = DropdownPage(driver)
        page.open()
        page.select_day("Wednesday")
        assert page.get_selected_day() == "Wednesday"
    finally:
        driver.quit()
