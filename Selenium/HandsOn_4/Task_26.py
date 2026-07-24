"""
Task 26 - implicit wait.

driver.implicitly_wait(10) is easy but not great practice: it applies globally for
every element lookup on the driver for the whole session, even ones that don't need
it, and it only checks that an element exists in the DOM, not that it's visible or
clickable. Explicit waits (Hands-On 5) let you wait for the actual condition you need,
on just the element that needs it.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    try:
        driver.get(PLAYGROUND_URL)
        print(driver.title)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
