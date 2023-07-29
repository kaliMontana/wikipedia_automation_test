import html
import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from pages.registration_page import RegistrationPage
from tests.conftest import wiki_base_url
from utils.api_utils import search_request_parameters

registration_page = RegistrationPage()
load_dotenv()


def request_to_login_page():
    login_page_response = requests.post(
        f'{wiki_base_url}{registration_page.log_in_page_path}{registration_page.log_in_page_auth_query}',
        allow_redirects=False
    )

    assert login_page_response.status_code == requests.codes.ok
    return login_page_response


def get_loginToken_from_response(login_page_response):
    response_parser = BeautifulSoup(html.unescape(login_page_response.text), 'html.parser')
    reponse_wpLoginToken = response_parser.select('input[name=wpLoginToken]')[0].get('value')
    return reponse_wpLoginToken


def request_for_authorization(reponse_wpLoginToken, cookies):
    authorization_response = requests.post(
        f'{wiki_base_url}{registration_page.log_in_page_path}{registration_page.log_in_page_auth_query}',
        data={
            "title": "Special:UserLogin",
            "wpName": os.getenv('wplogin'),
            "wpPassword": os.getenv("wpPassword"),
            "wploginattempt": "Log in",
            "wpEditToken": "+\\",
            "authAction": "login",
            "force": "",
            "wpLoginToken": reponse_wpLoginToken,
            "geEnabled": "-1",
            "forceMentor": ""
        },
        cookies=cookies,
        allow_redirects=False
    )

    assert authorization_response.status_code == requests.codes.found

    return authorization_response


def request_for_article_search(cookies):
    search_response = requests.get(
        f'{wiki_base_url}{registration_page.log_in_page_path}',
        params=search_request_parameters(),
        cookies=cookies,
        allow_redirects=True
    )

    assert search_response.status_code == requests.codes.ok

    return search_response
