from pages.api_pages import RegistarionThroughtApi
from pages.registration_page import RegistrationPage
from pages.user_main_page import UserMainPage

registration_page = RegistrationPage()
user_main_page = UserMainPage()
registarionThroughtApi = RegistarionThroughtApi()


def test_registration_ui():
    registration_page.open_login_page()
    registration_page.set_login()
    registration_page.set_password()
    registration_page.login_attempt()
    user_main_page.should_have_welcome_and_name()


def test_registration_through_api():
    login_page_response = registarionThroughtApi.request_login_page()
    reponse_wpLoginToken = registarionThroughtApi.get_loginToken_from_response(login_page_response)
    authorization_response = registarionThroughtApi.request_authorization(reponse_wpLoginToken,
                                                                          login_page_response.cookies)

    registration_page.open_user_main_page(authorization_response.cookies)
    user_main_page.should_have_welcome_and_name()
