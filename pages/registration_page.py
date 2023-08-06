import os
import time

import allure
from dotenv import load_dotenv

from utils.api_utils import set_response_cookies_to_browser


class RegistrationPage:
    load_dotenv()

    def __init__(self, browser):
        self.browser = browser
        self.log_in_page_path = '/w/index.php'
        self.log_in_page_auth_query = '?title=Special:UserLogin&returnto=Main+Page'
        self.user_main_page_path = '/wiki/Main_Page'
        self.login = 'input[id=wpName1]'
        self.password = 'input[id=wpPassword1]'
        self.login_attempt_button = 'button[id=wpLoginAttempt]'

    @allure.step('Open "Log in" page')
    def open_login_page(self):
        self.browser.open(f'{self.log_in_page_path}{self.log_in_page_auth_query}')

    @allure.step('Type login')
    def set_login(self):
        self.browser.element(self.login).send_keys(os.getenv('wplogin'))

    @allure.step('Type password')
    def set_password(self):
        self.browser.element(self.password).send_keys(os.getenv('wpPassword'))

    @allure.step('Click on button Log in')
    def login_attempt(self):
        self.browser.element(self.login_attempt_button).click()

    @allure.step('Open user main page')
    def open_user_main_page_and_set_cookies(self, cookies):
        self.browser.open(self.user_main_page_path)
        time.sleep(1)

        set_response_cookies_to_browser(self.browser, cookies)

        self.browser.open(self.user_main_page_path)
