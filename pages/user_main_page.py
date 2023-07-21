import os

import allure
from dotenv import load_dotenv
from selene import have
from selene.support.shared.jquery_style import s


class UserMainPage:
    load_dotenv()

    def __init__(self):
        self.welcome_wp = s('span[id=Welcome_to_Wikipedia]')
        self.your_home_page = s("a[title='Your homepage (page does not exist) [alt-shift-.]'] span")

    @allure.step('Check welcome title and user name in user main page')
    def should_have_welcome_and_name(self):
        assert self.welcome_wp.should(have.text('Welcome to'))
        assert self.your_home_page.should(have.exact_text(os.getenv('wplogin')))
