import html
import logging
import os
import time

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selene import browser, query

from pages.registration_page import RegistrationPage
from tests.conftest import wiki_base_url


def test_registration():
    registration_page = RegistrationPage(browser)

    registration_page.log_in(browser)
    value = browser.element('input[name=wpLoginToken]').get(query.attribute('value'))
    # value = browser.element(by.xpath("//input[@name='wpLoginToken']")).value_of_('value')
    # value = browser.element(by.xpath("//input[@name='wpLoginToken']")).get(query.attribute('value'))
    print('value: ' + value)
    browser.config.driver.get_cookies()
    logging.info(browser.config.driver.get_cookies())
    time.sleep(10)


def test_registration_ui():
    registration_page = RegistrationPage(browser)
    load_dotenv()

    registration_page.login_ui(browser)
    browser.element('input[id=wpName1]').send_keys(os.getenv('wplogin'))
    browser.element('input[id=wpPassword1]').send_keys(os.getenv('wpPassword'))
    browser.element('button[id=wpLoginAttempt]').click()
    logging.info(browser.config.driver.get_cookies())
    time.sleep(5)


def test_open_registration_page():
    registration_page = RegistrationPage(browser)
    load_dotenv()

    registration_page.log_in(browser)


response = requests.post(
    "https://en.wikipedia.org/w/index.php?title=Special:UserLogin",
    data={
        "title": "Special:UserLogin",
        "wpName": os.getenv('wplogin'),
        "wpPassword": os.getenv('wpPassword'),
        "wploginattempt": "Log in",
        "authAction": "login",

        "wpLoginToken": "",
        "geEnabled": "-1"
    },
    allow_redirects=False
)


def test_registration_with_api():
    logging.info(response.status_code)
    # logging.info(response.text)
    auth_cookie2 = response.cookies.get("ss0-centralauth_Session")
    logging.info(auth_cookie2)
    auth_cookie = response.cookies.get("wpLoginToken")
    logging.info(auth_cookie)

    # assert response.status_code == 302


def test_registration_with_api_2():
    registration_page = RegistrationPage(browser)
    load_dotenv()

    registration_page.log_in(browser)
    value = browser.element('input[name=wpLoginToken]').get(query.attribute('value'))
    # value = browser.element(by.xpath("//input[@name='wpLoginToken']")).value_of_('value')
    # value = browser.element(by.xpath("//input[@name='wpLoginToken']")).get(query.attribute('value'))
    print('value: ' + value)
    coo = browser.config.driver.get_cookies()
    driver = browser.config.driver
    logging.info(browser.config.driver.get_cookie('ss0-enwikiSession').get('value'))
    logging.info(browser.config.driver.get_cookie('enwikiSession').get('value'))
    logging.info(browser.config.driver.get_cookie('WMF-Last-Access').get('value'))
    logging.info(browser.config.driver.get_cookie('WMF-Last-Access-Global').get('value'))
    logging.info(browser.config.driver.get_cookie('GeoIP').get('value'))
    logging.info(browser.config.driver.get_cookie('NetworkProbeLimit').get('value'))
    logging.info(browser.config.driver.get_cookie('enwikimwuser-sessionId').get('value'))
    logging.info(browser.config.driver.get_cookie('enwikiwmE-sessionTickLastTickTime').get('value'))
    logging.info(browser.config.driver.get_cookie('enwikiwmE-sessionTickTickCount').get('value'))
    logging.info(browser.config.driver.get_cookies()[0].get("domain"))
    logging.info(browser.config.driver.get_cookies())

    # cookies_auth = {'ss0-enwikiSession': driver.get_cookie('ss0-enwikiSession').get('value'),
    #                 'enwikiSession': driver.get_cookie('enwikiSession').get('value'),
    #                 'WMF-Last-Access': driver.get_cookie('WMF-Last-Access').get('value'),
    #                 'WMF-Last-Access-Global': driver.get_cookie('WMF-Last-Access-Global').get('value'),
    #                 'GeoIP': driver.get_cookie('GeoIP').get('value'),
    #                 'NetworkProbeLimit': driver.get_cookie('NetworkProbeLimit').get('value'),
    #                 'enwikimwuser-sessionId': driver.get_cookie('enwikimwuser-sessionId').get('value'),
    #                 'enwikiwmE-sessionTickLastTickTime': driver.get_cookie('enwikiwmE-sessionTickLastTickTime').get('value'),
    #                 'enwikiwmE-sessionTickTickCount': driver.get_cookie('enwikiwmE-sessionTickTickCount').get('value')
    #                 }

    cookies_auth = {'enwikimwuser-sessionId': driver.get_cookie('enwikimwuser-sessionId').get('value'),
                    'enwikiSession': driver.get_cookie('enwikiSession').get('value'),
                    'enwikiwmE-sessionTickLastTickTime': driver.get_cookie('enwikiwmE-sessionTickLastTickTime').get(
                        'value'),
                    'enwikiwmE-sessionTickTickCount	': driver.get_cookie('enwikiwmE-sessionTickTickCount').get(
                        'value'),
                    'GeoIP': driver.get_cookie('GeoIP').get('value'),
                    'NetworkProbeLimit': driver.get_cookie('NetworkProbeLimit').get('value'),
                    'ss0-enwikiSession': driver.get_cookie('ss0-enwikiSession').get('value'),
                    'WMF-Last-Access': driver.get_cookie('WMF-Last-Access').get('value'),
                    'WMF-Last-Access-Global': driver.get_cookie('WMF-Last-Access-Global').get('value')
                    }

    response = requests.post(
        "https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page",
        data={
            "title": "Special:UserLogin",
            "wpName": os.getenv('wplogin'),
            "wpPassword": os.getenv('wpPassword'),
            "wploginattempt": "Log in",
            "wpEditToken": "+\\",
            "authAction": "login",
            "force": "",
            "wpLoginToken": value,
            "geEnabled": "-1",
            "forceMentor": ""
        },
        cookies=cookies_auth,
        allow_redirects=True
    )
    logging.info(response.status_code)
    logging.info(response.text)
    auth_cookie2 = response.cookies.get("enwikiSession")
    logging.info('enwikiSession: ' + auth_cookie2)
    auth_cookie = response.cookies.get("GeoIP")
    logging.info(response.cookies)


def test_registration_with_api_3():
    registration_page = RegistrationPage(browser)
    load_dotenv()

    login_page_response = requests.post(
        #"https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page",
        f'{wiki_base_url}{registration_page.log_in_page_path}',
        allow_redirects=False
    )
    logging.info(login_page_response.status_code)
    # logging.info(html.unescape(response0.text))

    response_parser = BeautifulSoup(html.unescape(login_page_response.text), 'html.parser')
    # logging.info(parse)

    reponse_wpLoginToken = response_parser.select('input[name=wpLoginToken]')[0].get('value')
    #logging.info(parse2)

    authorization_response = requests.post(
        #"https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page",
        f'{wiki_base_url}{registration_page.log_in_page_path}',
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
        cookies=login_page_response.cookies,
        allow_redirects=False
    )

    logging.info(authorization_response.status_code)
    #logging.info(html.unescape(authorization_response.text))
    logging.info(authorization_response.cookies)
    logging.info(requests.utils.dict_from_cookiejar(authorization_response.cookies))

    registration_page.user_main_page(authorization_response.cookies)
    time.sleep(5)

