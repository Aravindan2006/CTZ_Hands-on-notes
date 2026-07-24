from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import BASE_URL


class InputFormPage(BasePage):
    URL = BASE_URL + "input-form-demo"

    NAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[type='tel']")
    ADDRESS_INPUT = (By.NAME, "Address")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input.btn.btn-success")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success, .success-msg, h2.text-success")

    def open(self):
        self.navigate_to(self.URL)

    def fill_form(self, name, email, phone, address):
        self.wait_for_element(self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

    def submit_form(self):
        self.wait_for_clickable(self.SUBMIT_BUTTON).click()

    def get_success_message(self):
        return self.wait_for_element(self.SUCCESS_MESSAGE).text
