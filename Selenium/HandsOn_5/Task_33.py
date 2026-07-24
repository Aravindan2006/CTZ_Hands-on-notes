"""Task 33 - same element, three CSS selector styles."""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

SIMPLE_FORM_URL = "https://www.lambdatest.com/selenium-playground/simple-form-demo"


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(SIMPLE_FORM_URL)

        driver.find_element(By.CSS_SELECTOR, "#user-message")
        driver.find_element(By.CSS_SELECTOR, "[name='message']")
        driver.find_element(By.CSS_SELECTOR, "div.form-group > textarea")

        print("all three CSS selectors found the element")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
