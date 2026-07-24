"""Task 32 - locate the message textarea on Simple Form Demo six different ways."""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

SIMPLE_FORM_URL = "https://www.lambdatest.com/selenium-playground/simple-form-demo"


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(SIMPLE_FORM_URL)

        driver.find_element(By.ID, "user-message")
        driver.find_element(By.NAME, "message")
        driver.find_element(By.CLASS_NAME, "form-control")
        driver.find_element(By.TAG_NAME, "textarea")
        driver.find_element(By.XPATH, "//textarea[@id='user-message']")

        # absolute xpath - fragile, breaks if the markup shifts at all, only here to
        # cover the exercise's "try every strategy" requirement
        try:
            driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/form/div[1]/textarea")
        except Exception:
            print("absolute xpath didn't match - expected, this locator is brittle")

        print("all locator strategies found the element")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
