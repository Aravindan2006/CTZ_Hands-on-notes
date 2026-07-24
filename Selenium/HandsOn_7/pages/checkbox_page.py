from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import BASE_URL


class CheckboxPage(BasePage):
    URL = BASE_URL + "checkbox-demo"

    def open(self):
        self.navigate_to(self.URL)

    def _checkbox(self, index):
        locator = (By.CSS_SELECTOR, f"ul#checkboxes li:nth-child({index}) input")
        return self.wait_for_element(locator)

    def check_option(self, index):
        box = self._checkbox(index)
        if not box.is_selected():
            box.click()

    def uncheck_option(self, index):
        box = self._checkbox(index)
        if box.is_selected():
            box.click()

    def is_option_checked(self, index):
        return self._checkbox(index).is_selected()
