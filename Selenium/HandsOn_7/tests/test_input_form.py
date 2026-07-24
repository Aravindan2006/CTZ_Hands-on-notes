from pages.input_form_page import InputFormPage


def test_input_form_submit(driver):
    page = InputFormPage(driver)
    page.open()
    page.fill_form(
        name="Jane Doe",
        email="jane.doe@example.com",
        phone="9876543210",
        address="221B Baker Street, London",
    )
    page.submit_form()

    assert page.get_success_message()
