import html
import logging

import allure
from bs4 import BeautifulSoup

from tests.conftest import wiki_base_url
from utils.api_request_utils import request_to_login_page, request_for_authorization, get_loginToken_from_response, \
    request_for_article_search


class RegistrationThroughApi():
    def __init__(self):
        self.wiki_path = '/wiki/'
        self.page_article_title_selector = 'h1[id=firstHeading] span[class*=page-title-main]'

    @allure.step('Send request to lon in page')
    def request_login_page(self):
        login_page_response = request_to_login_page()
        return login_page_response

    @allure.step('Get loginToken from api response')
    def get_loginToken(self, login_page_response):
        reponse_wpLoginToken = get_loginToken_from_response(login_page_response)
        return reponse_wpLoginToken

    @allure.step('Send request for authorization')
    def request_authorization(self, reponse_wpLoginToken, cookies):
        authorization_response = request_for_authorization(reponse_wpLoginToken, cookies)
        return authorization_response

    @allure.step('Send request to search an article')
    def request_article_search(self, cookies, word_to_search):
        article_search_response = request_for_article_search(cookies, word_to_search)
        logging.info(article_search_response.url)
        return article_search_response

    @allure.step('Check url and tab, page titles')
    def check_page_title_and_url(self, article_search_response, page_article_title, word_to_search):
        response_parser = BeautifulSoup(html.unescape(article_search_response.text), 'html.parser')
        title_for_url = word_to_search.replace(' ', '_')

        assert article_search_response.url == f'{wiki_base_url}{self.wiki_path}{title_for_url}'
        assert response_parser.select('title')[0].text == page_article_title
        assert response_parser.select(self.page_article_title_selector)[0].text == word_to_search
