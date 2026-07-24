"""
Task 48 - base_url is a session-scoped fixture (in conftest.py), computed once and
reused across the whole test run instead of hardcoding the URL in every test.
"""


def test_base_url_fixture(base_url):
    assert base_url == "https://www.testmuai.com/selenium-playground/"


def test_navigate_with_base_url(driver, base_url):
    driver.get(base_url)
    assert driver.current_url.rstrip("/") == base_url.rstrip("/")
