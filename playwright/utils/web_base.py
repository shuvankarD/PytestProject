import token

from playwright.sync_api import Playwright

order_payload = {"orders": [{"country": "India" , "productOrderedId": "68a961459320a140fe1ca57a"}]}

class APIUtils:

    def get_token(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data="token"
                                            )
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def create_order(self, playwright: Playwright):

         token = self.get_token(playwright)

         api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
         response = api_request_context.post("/api/order/create",
                                             data =order_payload,
                                             headers = {"Authorization": token,
                                                 "Content-Type": "application/json"})

         print(response.json())

