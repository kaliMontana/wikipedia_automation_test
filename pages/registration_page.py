import logging
import time

from selene.support.shared import browser


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
        time.sleep(2)

        # logging.info(cookies.get('enwikiSession'))
        # logging.info(cookies.get('NetworkProbeLimit'))
        # logging.info(cookies.get('ss0-enwikiSession'))

        browser.driver.add_cookie({'name': 'enwikiSession', 'value': cookies.get('enwikiSession')})
        browser.driver.add_cookie({'name': 'enwikiUserID', 'value': cookies.get('enwikiUserID')})
        browser.driver.add_cookie({'name': 'enwikiUserName', 'value': cookies.get('enwikiUserName')})
        browser.driver.add_cookie({'name': 'loginnotify_prevlogins', 'value': cookies.get('loginnotify_prevlogins')})
        browser.driver.add_cookie({'name': 'cpPosIndex', 'value': cookies.get('cpPosIndex')})
        browser.driver.add_cookie({'name': 'UseDC', 'value': cookies.get('UseDC')})
        browser.driver.add_cookie({'name': 'NetworkProbeLimit', 'value': cookies.get('NetworkProbeLimit')})
        browser.driver.add_cookie({'name': 'centralauth_User', 'value': cookies.get('centralauth_User')})
        browser.driver.add_cookie({'name': 'centralauth_Session', 'value': cookies.get('centralauth_Session')})

        browser.open(self.user_main_page_path)
