"""
Task 46 - screenshot on failure.

The actual hook is in conftest.py (pytest_runtest_makereport). This test fails on
purpose so you can see it fire - check screenshots/ after running this.
"""

from selenium.webdriver.common.by import By


def test_intentional_failure_for_screenshot_demo(driver, base_url):
    driver.get(base_url + "checkbox-demo")
    heading = driver.find_element(By.TAG_NAME, "h1")
    assert heading.text == "this will never match"
