import json

from playwright.sync_api import Playwright

from utils.web_base import APIUtils


def test_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_utils = APIUtils()
    api_utils.create_order(playwright)

    # Open json file

    with open('external_data/credentials.json') as json_file:
        test_data = json.load(json_file)
        print(test_data)


    page.goto("https://rahulshettyacademy.com/client")

   #create Order
    page.get_by_placeholder("eamil@example.com").fill("rahulshetty@gmail.com")

    page.get_by_placeholder("enter your passsword").fill("Iamking@000")

    page.get_by_role("button", name="Login").click()