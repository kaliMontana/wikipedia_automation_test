import logging
import time

from selene.support.shared import browser

from utils.set_cookies import set_response_cookies_to_browser


class RegistrationPage:
    def __init__(self, browser):
        self.log_in_page_path = '/w/index.php?title=Special:UserLogin&returnto=Main+Page'
        self.user_main_page_path = '/wiki/Main_Page'

    def log_in(self, browser):
        browser.open(self.log_in_page_path)

    def login_ui(self, browser):
        browser.open(self.log_in_page_path)
        browser

    def user_main_page(self, cookies):
        browser.open(self.user_main_page_path)
        time.sleep(1)

        set_response_cookies_to_browser(cookies)

        browser.open(self.user_main_page_path)
