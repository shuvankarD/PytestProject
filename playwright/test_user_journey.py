from playwright.sync_api import Page
from playwright.sync_api import expect


def test_user_journey(page : Page):

    #Login functionalities
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("Teacher")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

    #Add Items into cart
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    nokia_product = page.locator("app-card").filter(has_text="nokia Edge")
    nokia_product.get_by_role("button").click()

    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

