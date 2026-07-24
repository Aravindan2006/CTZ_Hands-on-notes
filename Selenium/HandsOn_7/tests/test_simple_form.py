from pages.simple_form_page import SimpleFormPage


def test_simple_form_submission(driver):
    page = SimpleFormPage(driver)
    page.open()
    page.enter_message("Hello Selenium")
    page.click_submit()

    assert page.get_displayed_message() == "Hello Selenium"
