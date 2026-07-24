from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from utils.config import BASE_URL


class DropdownPage(BasePage):
    URL = BASE_URL + "select-dropdown-demo"
    DAY_DROPDOWN = (By.ID, "select-demo")

    def open(self):
        self.navigate_to(self.URL)

    def select_day(self, day_name):
        Select(self.wait_for_element(self.DAY_DROPDOWN)).select_by_visible_text(day_name)

    def get_selected_day(self):
        return Select(self.wait_for_element(self.DAY_DROPDOWN)).first_selected_option.text
