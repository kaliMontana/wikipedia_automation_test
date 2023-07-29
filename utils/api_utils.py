import os

from selene.support.shared import browser


def set_response_cookies_to_browser(cookies):
    browser.driver.add_cookie({'name': 'enwikiSession', 'value': cookies.get('enwikiSession')})
    browser.driver.add_cookie({'name': 'enwikiUserID', 'value': cookies.get('enwikiUserID')})
    browser.driver.add_cookie({'name': 'enwikiUserName', 'value': cookies.get('enwikiUserName')})
    browser.driver.add_cookie({'name': 'loginnotify_prevlogins', 'value': cookies.get('loginnotify_prevlogins')})
    browser.driver.add_cookie({'name': 'cpPosIndex', 'value': cookies.get('cpPosIndex')})
    browser.driver.add_cookie({'name': 'UseDC', 'value': cookies.get('UseDC')})
    browser.driver.add_cookie({'name': 'NetworkProbeLimit', 'value': cookies.get('NetworkProbeLimit')})
    browser.driver.add_cookie({'name': 'centralauth_User', 'value': cookies.get('centralauth_User')})
    browser.driver.add_cookie({'name': 'centralauth_Session', 'value': cookies.get('centralauth_Session')})


def auth_request_parameters(reponse_wpLoginToken):
    return {
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
    }


def search_request_parameters():
    return {
        "search": "Wikimedia Foundation",
        "title": 'Special:Search',
        "wprov": 'acrw1_-1'
    }
