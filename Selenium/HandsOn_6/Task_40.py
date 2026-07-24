"""Task 40 - pytest picks up any function starting with test_."""

from selenium.webdriver.common.by import By


def test_playground_loads(driver, base_url):
    driver.get(base_url)
    assert driver.title


def test_checkbox_interaction(driver, base_url):
    driver.get(base_url + "checkbox-demo")
    box = driver.find_element(By.ID, "isAgeSelected")
    box.click()
    assert box.is_selected()
