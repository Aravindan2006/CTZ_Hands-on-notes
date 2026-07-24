"""Task 36 - click Success on the Bootstrap Alerts page, wait for the alert, check the text."""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

ALERTS_URL = "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo"


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(ALERTS_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Success')]"))).click()
        alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))

        assert "successfully" in alert.text.lower()
        print(alert.text)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
