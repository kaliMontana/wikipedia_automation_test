import allure
from selene import have
from selene.support.shared.jquery_style import s


class ArticlePage:

    def __init__(self):
        self.page_title_main = s('h1[id=firstHeading] span[class*=page-title-main]')

    @allure.step('Check the page title main {title}')
    def check_page_title(self, title):
        self.page_title_main.should(have.exact_text(title))
