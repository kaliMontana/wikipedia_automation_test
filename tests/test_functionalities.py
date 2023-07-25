import time

import allure
from allure_commons.types import Severity

from pages.api_pages import RegistrationThroughApi
from pages.article_page import ArticlePage
from pages.registration_page import RegistrationPage
from pages.user_main_page import UserMainPage
from pages.watch_list_page import WatchListPage

registration_page = RegistrationPage()
user_main_page = UserMainPage()
article_page = ArticlePage()
watchListPage = WatchListPage()

registrationThroughApi = RegistrationThroughApi()

WORD_TO_SEARCH = 'Wikimedia Foundation'


@allure.tag('UI version')
@allure.severity(Severity.CRITICAL)
@allure.feature('User interface authorization')
@allure.title('Authorization')
def test_authorization_ui():
    registration_page.open_login_page()
    registration_page.set_login()
    registration_page.set_password()
    registration_page.login_attempt()
    user_main_page.should_have_welcome_and_name()


@allure.tag('UI version')
@allure.severity(Severity.CRITICAL)
@allure.feature('Search')
@allure.title('UI Search')
def test_search_ui():
    registration_page.open_login_page()
    registration_page.set_login()
    registration_page.set_password()
    registration_page.login_attempt()
    user_main_page.should_have_welcome_and_name()

    user_main_page.search(WORD_TO_SEARCH)
    article_page.check_page_title(WORD_TO_SEARCH)


@allure.tag('UI version')
@allure.severity(Severity.CRITICAL)
@allure.feature('Add article to watch list')
@allure.title('UI Add article')
def test_add_article_ui():
    registration_page.open_login_page()
    registration_page.set_login()
    registration_page.set_password()
    registration_page.login_attempt()
    user_main_page.should_have_welcome_and_name()

    user_main_page.search(WORD_TO_SEARCH)
    article_page.check_page_title(WORD_TO_SEARCH)

    article_page.add_article()
    article_page.go_to_watch_list()
    watchListPage.check_page_title()
    watchListPage.go_to_view_and_edit_watch_list()
    watchListPage.check_if_page_title_is_in_list(WORD_TO_SEARCH)


@allure.tag('API version')
@allure.severity(Severity.CRITICAL)
@allure.feature('Api authorization')
@allure.title('Authorization')
def test_authorization_through_api():
    login_page_response = registrationThroughApi.request_login_page()
    reponse_wpLoginToken = registrationThroughApi.get_loginToken(login_page_response)
    authorization_response = registrationThroughApi.request_authorization(reponse_wpLoginToken,
                                                                          login_page_response.cookies)

    registration_page.open_user_main_page_and_set_cookies(authorization_response.cookies)
    user_main_page.should_have_welcome_and_name()
