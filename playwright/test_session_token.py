from playwright.sync_api import Page, expect, Playwright

from utils.web_base import APIUtils


def test_session_token(playwright : Playwright):

    api_utils = APIUtils()
    getToken= api_utils.get_token(playwright)

    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.add_init_script(f""""localStorage.setItem('token', '{getToken}')""")

    page.goto("https://rahulshettyacademy.com/client")

    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders'))
