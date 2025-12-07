from playwright.sync_api import Playwright


def test_API_flow (playwright: Playwright):

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://rahulshettyacademy.com/client")

    page.get_by_placeholder("email@emaxple.com").fill("shuvo@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Hofbeatles123!")
    page.get_by_role("button", name="Login").click()
