from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_simple_form_submission(driver, base_url):
    driver.get(base_url + "simple-form-demo")

    driver.find_element(By.ID, "user-message").send_keys("Hello Selenium")
    driver.find_element(By.ID, "showInput").click()

    message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "message")))
    assert message.text == "Hello Selenium"
