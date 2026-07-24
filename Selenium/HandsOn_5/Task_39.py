"""Task 39 - fluent-style wait: poll every 500ms, up to 10s, ignore NoSuchElementException."""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

TABLE_URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get(TABLE_URL)

        wait = WebDriverWait(driver, 10, poll_frequency=0.5, ignored_exceptions=[NoSuchElementException])
        row = wait.until(lambda d: d.find_element(By.CSS_SELECTOR, "table#productTable tbody tr"))
        print(row.text)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
