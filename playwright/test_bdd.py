from playwright.utils.web_base import APIUtils
from pytest_bdd import scenarios, given, when, then

scenarios('features/orders.feature')


@given('place the order with <username> and <password>'):

    def place_order(playwright,username, password):
        user_credentials = {}
        user_credentials["username"] = username
        user_credentials["password"] = password
        api_utils = APIUtils()
        order_id = api_utils.create_order(playwright, user_credentials)

@given('the user is on landing page'):

    def user_is_on_landing_page(playwright, browser_instance):
        login_page = browser_instance.get_page("login")
        login_page.navigate()

@when('login in portal with <username> and <password>'):
    def login_in_portal(playwright, username, password):
        shared = shared.get_shared()
        shared.login(username, password)

@when('navigate to order page'):
   def navigate_to_order_page(playwright):
       shared = shared.get_shared()

@when('Select the order'):
   def select_order(playwright):
       shared = shared.get_shared()

@then('Order message is displayed'):
     def order_message(playwright):
