import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission_parametrized(driver, base_url, message):
    driver.get(base_url + "simple-form-demo")

    driver.find_element(By.ID, "user-message").send_keys(message)
    driver.find_element(By.ID, "showInput").click()

    displayed = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "message")))
    assert displayed.text == message
