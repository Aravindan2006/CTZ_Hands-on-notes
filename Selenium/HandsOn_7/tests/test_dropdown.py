from pages.dropdown_page import DropdownPage


def test_dropdown_selection(driver):
    page = DropdownPage(driver)
    page.open()
    page.select_day("Wednesday")

    assert page.get_selected_day() == "Wednesday"
