"""
Task 41 - the driver fixture lives in conftest.py (scope='function', so every test
gets a fresh browser). Tests just take `driver` as a parameter, pytest handles the
setup/teardown.
"""


def test_driver_fixture_works(driver, base_url):
    driver.get(base_url)
    assert driver.current_url.startswith("https://www.testmuai.com")