from playwright.sync_api import Playwright

orders_payload= {"orders": [{"country": "British Indian Ocean Territory", "productOrderedId": "68a961459320a140fe1ca57a"}]}

class APIUtils:

    def create_token(self, playwright: Playwright):
        token_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = token_request_context.post("/api/ecom/auth/login",
                                   data={"userEmail": "shuvo@gmail.com", "userPassword": "Hofbeatles123!"})
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def create_order(self, playwright:Playwright):

        token = self.create_token(playwright)

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("/api/ecom/auth/order",
                                            data=orders_payload,
                                            headers={"Content-Type": "application/json", "Authorization": token }
                                            )

        print(response.json())