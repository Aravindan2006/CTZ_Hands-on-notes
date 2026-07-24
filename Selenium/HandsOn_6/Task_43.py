from selenium.webdriver.common.by import By


def test_checkbox_demo(driver, base_url):
    driver.get(base_url + "checkbox-demo")

    checkbox = driver.find_element(By.ID, "isAgeSelected")
    checkbox.click()
    assert checkbox.is_selected()

    checkbox.click()
    assert not checkbox.is_selected()