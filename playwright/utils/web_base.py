
from playwright.sync_api import Playwright

orders_payload= {"orders": [{"country": "British Indian Ocean Territory", "productOrderedId": "68a961459320a140fe1ca57a"}]}

class APIUtils:

    def get_token(self, playwright: Playwright):
       api_get_token = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
       response = api_get_token.post("/api/ecom/auth/login",
                                     data={"userEmail": "shuvo@gmail.com", "userPassword": "Hofbeatles123!"})

       assert response.ok
       print(response.json())
       response_body = response.json()
       print(response_body)
       token = response_body["token"]
       return token


    def create_order(self, playwright:Playwright):

        token = self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response =api_request_context.post("/api/ecom/order-order",
                                 data=orders_payload,
                                 headers = {"Authorization": token, "Content-Type": "application/json"}
        )

        print(response.json())