"""
Task 31 - window sizing.

Setting a fixed window size matters because responsive layouts change what's on the
page (nav bars collapse into hamburger menus, elements reflow) depending on viewport
width. If tests run at whatever size the window happens to open at, locators that work
locally can fail in CI or vice versa.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(PLAYGROUND_URL)
        print("before:", driver.get_window_size())

        driver.set_window_size(1280, 800)
        print("after:", driver.get_window_size())
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
