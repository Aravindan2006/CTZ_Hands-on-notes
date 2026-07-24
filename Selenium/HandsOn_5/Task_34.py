"""Task 34 - XPath text() and contains() on the checkbox labels."""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

CHECKBOX_URL = "https://www.lambdatest.com/selenium-playground/checkbox-demo"


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(CHECKBOX_URL)

        first = driver.find_element(By.XPATH, "//label[text()='Option 1']")
        print(first.text)

        all_options = driver.find_elements(By.XPATH, "//label[contains(text(),'Option')]")
        for opt in all_options:
            print(opt.text)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
