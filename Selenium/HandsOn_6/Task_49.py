from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


def test_dropdown_selection(driver, base_url):
    driver.get(base_url + "select-dropdown-demo")

    dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "select-demo")))
    select = Select(dropdown)
    select.select_by_visible_text("Wednesday")

    assert select.first_selected_option.text == "Wednesday"
