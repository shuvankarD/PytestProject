from playwright.sync_api import Playwright

from utils.web_base import APIUtils


def test_API_flow(playwright:Playwright):

    #login functionality
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create order -> Order Id
    api_utils = APIUtils()
    api_utils.create_order(playwright)


    page.goto("https://rahulshettyacademy.com/client")

    page.get_by_placeholder("email@emaxple.com").fill("shuvo@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Hofbeatles123!")
    page.get_by_role("button", name="Login").click()

