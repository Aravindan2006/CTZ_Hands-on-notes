from pages.checkbox_page import CheckboxPage


def test_checkbox_demo(driver):
    page = CheckboxPage(driver)
    page.open()

    page.check_option(1)
    assert page.is_option_checked(1)

    page.uncheck_option(1)
    assert not page.is_option_checked(1)
