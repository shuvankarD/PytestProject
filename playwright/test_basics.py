import time

from pytest_playwright.pytest_playwright import browser

from playwright.sync_api import Page

# For multiple context
def test_basics(playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page= context.new_page()
    page.goto("https://rahulshettyacademy.com")

# chromium headless, one single context
def test_shortcut(page:Page):
    page.goto("https://www.linkedin.com/in/shuvankar-dash/")


def test_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    time.sleep(5)
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)