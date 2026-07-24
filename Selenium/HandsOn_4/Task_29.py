"""Task 29 - open a new tab, switch to it, print its title."""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(PLAYGROUND_URL)
        driver.execute_script("window.open('https://www.google.com');")

        print(driver.window_handles)
        driver.switch_to.window(driver.window_handles[1])
        print(driver.title)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
