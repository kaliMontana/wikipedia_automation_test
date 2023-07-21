import allure

from utils.api_utils import request_to_login_page, request_for_authorization, get_loginToken_from_response


class RegistrationThroughApi():

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
