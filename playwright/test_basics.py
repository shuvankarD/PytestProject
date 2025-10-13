import time

from playwright.sync_api import Page, expect, Playwright


# For multiple context
def test_basics(playwright : Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page= context.new_page()
    page.goto("https://rahulshettyacademy.com")

# chromium headless, one single context
def test_shortcut(page:Page):
    page.goto("https://www.linkedin.com/in/shuvankar-dash/")

# Experimenting locators and methods
def test_locators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learninggg")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

    result = page.get_by_text("Incorrect username/password.")
    expect(result).to_be_visible()

# Running the tests on firefox
def test_firefox(playwright : Playwright):

    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learninggg")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

    result = page.get_by_text("Incorrect username/password.")
    expect(result).to_be_visible()