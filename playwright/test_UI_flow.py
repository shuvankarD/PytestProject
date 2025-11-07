from playwright.sync_api import Page
from playwright.sync_api import expect

def test_UI_check(page : Page):

    #Placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Alter Boxs

    page.locator("#confirmbtn").click()
    page.on("dialog", lambda dialog: dialog.accept())

    #Frame handling

    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("link", name="All Access plan").click()

    expect(page_frame.locator("body")).to_contain_text("Happy Subscibers")


