from playwright.sync_api import Playwright

orders_payload = {
    "orders": [
        {
            "country": "British Indian Ocean Territory",
            "productOrderedId": "68a961459320a140fe1ca57a"
        }
    ]
}

class APIUtils:

    def get_token(self, playwright: Playwright):
        request_context = playwright.request.new_context(
            base_url="https://rahulshettyacademy.com/client"
        )

        response = request_context.post(
            "/api/ecom/auth/login",
            data={
                "userEmail": "shuvo@gmail.com",
                "userPassword": "Hofbeatles123!"
            }
        )

        assert response.ok
        response_body = response.json()
        return response_body["token"]

    def create_order(self, playwright: Playwright):
        token = self.get_token(playwright)

        request_context = playwright.request.new_context(
            base_url="https://rahulshettyacademy.com/client"
        )

        response = request_context.post(
            "/api/ecom/order/create-order",
            data=orders_payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
        )

        assert response.ok
        print(response.json())
        return response.json()
