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


def test_dynamic_UI(page : Page):

    #Check the price of rice
    #Identify the price column
    #Indentify the rice column
    #Extract the price of Rice

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            col_value = index
            print(f"Price column value is {col_value} ")
            break

    rice_row = page.locator("tr").filter(has_text="Rice")

    expect(rice_row.locator("td").nth(col_value)).to_have_text("37")


def test_mouse_hover(page : Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()






