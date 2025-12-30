import time

from playwright.sync_api import Page

#fake_response = {"data":[],"message":"No Orders"}

# def intercept_response(route):
#     route.fulfill(
#         json=fake_response
#     )
def intercept_request(route):
   route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=/6953a7cdc941646b7a706b98")


def test_network(page: Page):

    page.goto("https://rahulshettyacademy.com/client")

   #page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id= *", intercept_request)

    page.get_by_placeholder("email@example.com").fill("shuvo@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Hofbeatles123!")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="VIEW").first.click()

    time.sleep(5)

    message = page.locator(".blink_me").text_content()
    print(message)

