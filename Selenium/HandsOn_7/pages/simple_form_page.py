from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import BASE_URL


class SimpleFormPage(BasePage):
    URL = BASE_URL + "simple-form-demo"

    MESSAGE_INPUT = (By.ID, "user-message")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#user-message + button")
    DISPLAYED_MESSAGE = (By.ID, "message")

    def open(self):
        self.navigate_to(self.URL)

    def enter_message(self, text):
        box = self.wait_for_element(self.MESSAGE_INPUT)
        box.clear()
        box.send_keys(text)

    def click_submit(self):
        self.wait_for_clickable(self.SUBMIT_BUTTON).click()

    def get_displayed_message(self):
        return self.wait_for_element(self.DISPLAYED_MESSAGE).text
