import allure
from selene import have, be
from selene.core.exceptions import TimeoutException


class ArticlePage:

    def __init__(self, browser):
        self.browser = browser
        self.page_title_main = 'h1[id=firstHeading] span[class*=page-title-main]'
        self.add_article_to_watchlist = '#ca-watch a[title*="Add this page"]'
        self.delete_article_to_watchlist_unstart = '#ca-unwatch a[title*="Remove this page"]'
        self.go_to_watch_list_page = "#pt-watchlist-2 a[title*='The list of pages']"
        self.add_star_icon_selector = '#ca-watch a[title*="Add this page"]'

    @allure.step('Check that the article page have title {title}')
    def check_page_title(self, title):
        self.browser.element(self.page_title_main).should(have.exact_text(title))

    @allure.step('Add article to watch list')
    def add_article(self):
        if self.is_element_present(self.add_star_icon_selector):
            self.browser.element(self.add_article_to_watchlist).click()
        else:
            self.browser.element(self.delete_article_to_watchlist_unstart).click()
            self.browser.element(self.add_article_to_watchlist).click()

    @allure.step('Go to watch list')
    def go_to_watch_list(self):
        self.browser.element(self.go_to_watch_list_page).click()

    def is_element_present(self, selector):
        try:
            self.browser.element(selector).should(be.present)
            return True
        except TimeoutException:
            return False
