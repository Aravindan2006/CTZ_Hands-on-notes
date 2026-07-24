import pytest

from utils.config import BASE_URL
from utils.helpers import build_chrome_driver


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture
def driver():
    chrome_driver = build_chrome_driver()
    yield chrome_driver
    chrome_driver.quit()
