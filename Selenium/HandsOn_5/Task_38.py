"""
Task 38 - element_to_be_clickable vs visibility_of_element_located.

visibility_of_element_located just checks the element is present and has a size (not
display:none). element_to_be_clickable checks that too, plus that it's enabled. Use
the clickable one when you're about to click something, visibility is enough when
you're just reading text off the page.
"""

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

        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Success')]")))
        button.click()

        alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))
        print(alert.text)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
