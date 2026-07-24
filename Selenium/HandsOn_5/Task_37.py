"""
Task 37 - time.sleep(3) vs WebDriverWait, timed side by side.

This is the one place in the whole project that uses time.sleep() - on purpose, to
show why it's worse than an explicit wait.
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

ALERTS_URL = "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo"


def with_sleep(driver):
    driver.get(ALERTS_URL)
    start = time.perf_counter()

    driver.find_element(By.XPATH, "//button[contains(text(),'Success')]").click()
    time.sleep(3)  # always waits 3s flat, whether the alert took 200ms or would've taken 4s
    alert = driver.find_element(By.CSS_SELECTOR, ".alert-success")

    return time.perf_counter() - start, alert.text


def with_wait(driver):
    driver.get(ALERTS_URL)
    start = time.perf_counter()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Success')]"))).click()
    alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))

    return time.perf_counter() - start, alert.text


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        t1, _ = with_sleep(driver)
        t2, _ = with_wait(driver)
        print(f"sleep: {t1:.2f}s, explicit wait: {t2:.2f}s")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
