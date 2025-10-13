import time

from playwright.sync_api import Page, expect


def test_UI_validation(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # verify two items are available
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

    iphone_phone = page.locator("app-card").filter(has_text="iphone X")
    iphone_phone.get_by_role("button", name="Add").click()

    nokia_phone = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_phone.get_by_role("button",name="Add").click()

    page.get_by_text("Checkout").click()

    result = page.locator(".media-body")

    expect(result).to_have_count(2)

    time.sleep(10)

# Double window tests
def test_child_page(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as popup:
        page.locator(".blinkingText").click()
        child_page = popup.value
        text = child_page.locator(".red").text_content()
        print(text)

