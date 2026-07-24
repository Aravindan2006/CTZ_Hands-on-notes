"""Task 25 - open Chrome, print the title, close it."""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(PLAYGROUND_URL)
        print(driver.title)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
