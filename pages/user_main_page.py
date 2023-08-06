import os

import allure
from dotenv import load_dotenv
from selene import have


class UserMainPage:
    load_dotenv()

    def __init__(self, browser):
        self.browser = browser
        self.welcome_wp = 'span[id=Welcome_to_Wikipedia]'
        self.your_home_page = "a[title='Your homepage (page does not exist) [alt-shift-.]'] span"
        self.search_input = 'form[id=searchform] input[class~=cdx-text-input__input]'
        self.search_button = '#searchform button[class~=cdx-button]'
        self.welcome_to = 'Welcome to'
        self.wplogin = 'wplogin'

    @allure.step('Check welcome title and user name in user main page')
    def should_have_welcome_and_user_name(self):
        assert self.browser.element(self.welcome_wp).should(have.text(self.welcome_to))
        assert self.browser.element(self.your_home_page).should(have.exact_text(os.getenv(self.wplogin)))

    @allure.step("Search '{search}'")
    def search(self, search):
        self.browser.element(self.search_input).type(search)
        self.browser.element(self.search_button).click()
