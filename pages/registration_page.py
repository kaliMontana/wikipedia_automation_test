import os
import time

from dotenv import load_dotenv
from selene.support.shared import browser

from utils.set_cookies import set_response_cookies_to_browser


class RegistrationPage:
    load_dotenv()

    def __init__(self):
        self.log_in_page_path = '/w/index.php?title=Special:UserLogin&returnto=Main+Page'
        self.user_main_page_path = '/wiki/Main_Page'
        self.login = browser.element('input[id=wpName1]')
        self.password = browser.element('input[id=wpPassword1]')
        self.login_attempt_button = browser.element('button[id=wpLoginAttempt]')

    def log_in(self):
        browser.open(self.log_in_page_path)

    def open_login_page(self):
        browser.open(self.log_in_page_path)

    def set_login(self):
        self.login.send_keys(os.getenv('wplogin'))

    def set_password(self):
        self.password.send_keys(os.getenv('wpPassword'))

    def login_attempt(self):
        self.login_attempt_button.click()

    def set_cookies_in_user_main_page(self, cookies):
        browser.open(self.user_main_page_path)
        time.sleep(1)

        set_response_cookies_to_browser(cookies)

        browser.open(self.user_main_page_path)
