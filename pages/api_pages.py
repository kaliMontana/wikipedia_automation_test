from utils.api_utils import request_to_login_page, get_loginToken_from_response, request_for_authorization


class RegistarionThroughtApi():

    def request_login_page(self):
        login_page_response = request_to_login_page()
        return login_page_response

    def get_loginToken_from_response(self, login_page_response):
        reponse_wpLoginToken = get_loginToken_from_response(login_page_response)
        return reponse_wpLoginToken

    def request_authorization(self, reponse_wpLoginToken, cookies):
        authorization_response = request_for_authorization(reponse_wpLoginToken, cookies)
        return authorization_response
