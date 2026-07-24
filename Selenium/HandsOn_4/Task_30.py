"""Task 30 - switch back to the first tab and take a screenshot."""

import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(PLAYGROUND_URL)
        driver.execute_script("window.open('https://www.google.com');")
        driver.switch_to.window(driver.window_handles[0])

        path = os.path.join(os.path.dirname(__file__), "playground_screenshot.png")
        driver.save_screenshot(path)
        print("saved:", path)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
