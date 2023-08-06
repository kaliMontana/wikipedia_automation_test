import allure
from selene import have


class WatchListPage:
    def __init__(self, browser):
        self.browser = browser
        self.page_title_main = 'h1[id=firstHeading]'
        self.view_and_edit_watch_list = "a[href='/wiki/Special:EditWatchlist']"
        self.article_list = 'div[id=mw-htmlform-ns0] span[class=oo-ui-labelElement-label]'
        self.page_title_watchlist = 'Watchlist'
        self.page_title_edit_watchlist = 'Edit watchlist'

    @allure.step("Check the page title 'Watchlist'")
    def check_page_title(self):
        self.browser.element(self.page_title_main).should(have.exact_text(self.page_title_watchlist))

    @allure.step("Go to 'View and edit watch list'")
    def go_to_view_and_edit_watch_list(self):
        self.browser.element(self.view_and_edit_watch_list).click()
        self.browser.element(self.page_title_main).should(have.exact_text(self.page_title_edit_watchlist))

    @allure.step("Check if the article was added")
    def check_if_page_title_is_in_list(self, title):
        self.browser.all(self.article_list).should(have.size_greater_than(0))
        self.browser.all(self.article_list).element_by(have.exact_text(title))
