import pytest
from dotenv import load_dotenv
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height1080 = 1080
    browser.config.base_url = 'https://en.wikipedia.org'
    yield
    browser.quit()
