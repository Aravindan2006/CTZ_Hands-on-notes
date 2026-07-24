"""Task 28 - navigate to Simple Form Demo, check the URL, go back."""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(PLAYGROUND_URL)
        driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

        assert "simple-form-demo" in driver.current_url
        print("on:", driver.current_url)

        driver.back()
        print("back to:", driver.current_url)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
