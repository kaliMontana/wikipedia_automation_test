import os

import pytest
from dotenv import load_dotenv
from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach

wiki_base_url = 'https://en.wikipedia.org'
DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version', default='100.0')
    parser.addoption(
        '--environment', default='remote'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_setup(request):
    if request.config.getoption('--environment') == 'local':
        from selene import browser

        browser.config.window_width = 1920
        browser.config.window_height1080 = 1080
        browser.config.base_url = wiki_base_url
        yield browser

        attach.add_html(browser)
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_video(browser)
        browser.quit()
    else:
        browser_version = request.config.getoption('--browser_version')
        browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')

        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub/",
            options=options
        )
        browser = Browser(Config(driver=driver, base_url=wiki_base_url, window_width=1920, window_height=1080))

        yield browser

        attach.add_html(browser)
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_video(browser)
        browser.quit()
