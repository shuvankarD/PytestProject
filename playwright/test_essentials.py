from playwright.sync_api import Playwright
from playwright.sync_api import Page
from playwright.sync_api import expect


def test_playwright_essential(playwright : Playwright):

    browser =playwright.chromium.launch(headless=False)
    context =browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

def test_playwright_shortcut(page:Page):
    page.goto("https://google.com")

def test_basics_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learninggg")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

    expect(page.get_by_text("Incorrect username/password")).to_be_visible()

def test_firefox_browser(playwright : Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com")

