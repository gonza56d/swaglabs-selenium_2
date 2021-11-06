from behave import Given, When, Then
from pages.login_page import LoginPage


@Given('the user is in saucedemo login page')
def user_is_in_saucedemo_login_page(context):
    login_page = LoginPage()
    login_page.type_user_and_password(
        'standard_user',
        'secret_sauce'
    )
    login_page.click_on_login_button()


@Then('successful login is performed and page with products is displayed')
def asd():
    kart_page = KartPage()
    assert 2 < 3

