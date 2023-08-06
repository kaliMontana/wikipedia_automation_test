import allure
from allure_commons.types import Severity

from pages.article_page import ArticlePage
from pages.registration_page import RegistrationPage
from pages.user_main_page import UserMainPage
from pages.watch_list_page import WatchListPage

WORD_TO_SEARCH = 'Wikimedia Foundation'
PAGE_ARTICLE_TITLE = 'Wikimedia Foundation - Wikipedia'


@allure.tag('UI version')
@allure.severity(Severity.CRITICAL)
@allure.feature('User interface authorization')
@allure.title('User authorization through user interface')
def test_authorization_ui(browser_setup):
    registration_page = RegistrationPage(browser_setup)
    registration_page.open_login_page()
    user_main_page = UserMainPage(browser_setup)

    registration_page.set_login()
    registration_page.set_password()
    registration_page.login_attempt()
    user_main_page.should_have_welcome_and_user_name()


@allure.tag('UI version')
@allure.severity(Severity.CRITICAL)
@allure.feature('Search')
@allure.title('Search a article')
def test_search_ui(browser_setup):
    registration_page = RegistrationPage(browser_setup)
    user_main_page = UserMainPage(browser_setup)
    article_page = ArticlePage(browser_setup)

    registration_page.open_login_page()
    registration_page.set_login()
    registration_page.set_password()
    registration_page.login_attempt()
    user_main_page.should_have_welcome_and_user_name()

    user_main_page.search(WORD_TO_SEARCH)
    article_page.check_page_title(WORD_TO_SEARCH)


@allure.tag('UI version')
@allure.severity(Severity.CRITICAL)
@allure.feature('Add article to watch list')
@allure.title('Add article')
def test_add_article_ui(browser_setup):
    registration_page = RegistrationPage(browser_setup)
    user_main_page = UserMainPage(browser_setup)
    article_page = ArticlePage(browser_setup)
    watchListPage = WatchListPage(browser_setup)

    registration_page.open_login_page()
    registration_page.set_login()
    registration_page.set_password()
    registration_page.login_attempt()
    user_main_page.should_have_welcome_and_user_name()

    user_main_page.search(WORD_TO_SEARCH)
    article_page.check_page_title(WORD_TO_SEARCH)

    article_page.add_article()
    article_page.go_to_watch_list()
    watchListPage.check_page_title()
    watchListPage.go_to_view_and_edit_watch_list()
    watchListPage.check_if_page_title_is_in_list(WORD_TO_SEARCH)
