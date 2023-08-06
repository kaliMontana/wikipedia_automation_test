import allure
from allure_commons.types import Severity

from pages.api_pages import RegistrationThroughApi
from pages.registration_page import RegistrationPage
from pages.user_main_page import UserMainPage

WORD_TO_SEARCH = 'Wikimedia Foundation'
PAGE_ARTICLE_TITLE = 'Wikimedia Foundation - Wikipedia'


@allure.tag('API version')
@allure.severity(Severity.CRITICAL)
@allure.feature('Api authorization')
@allure.title('User authorization through API')
def test_authorization_through_api(browser_setup):
    registration_through_api = RegistrationThroughApi()
    registration_page = RegistrationPage(browser_setup)
    user_main_page = UserMainPage(browser_setup)

    login_page_response = registration_through_api.request_login_page()
    reponse_wpLoginToken = registration_through_api.get_loginToken(login_page_response)
    authorization_response = registration_through_api.request_authorization(reponse_wpLoginToken,
                                                                            login_page_response.cookies)

    registration_page.open_user_main_page_and_set_cookies(authorization_response.cookies)
    user_main_page.should_have_welcome_and_user_name()


@allure.tag('API version')
@allure.severity(Severity.CRITICAL)
@allure.feature('Api Search article')
@allure.title('Search article through API')
def test_search_article_through_api():
    registration_through_api = RegistrationThroughApi()

    login_page_response = registration_through_api.request_login_page()
    reponse_wpLoginToken = registration_through_api.get_loginToken(login_page_response)
    registration_through_api.request_authorization(reponse_wpLoginToken,
                                                   login_page_response.cookies)

    search_response = registration_through_api.request_article_search(login_page_response.cookies, WORD_TO_SEARCH)
    registration_through_api.check_page_title_and_url(search_response, PAGE_ARTICLE_TITLE, WORD_TO_SEARCH)
