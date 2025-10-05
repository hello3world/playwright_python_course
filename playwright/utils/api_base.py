from playwright.sync_api import Playwright

orders_payload = {"orders":[{"country":"Belarus","productOrderedId":"68a961719320a140fe1ca57c"}]}


class ApiUtils:
    def get_access_token(self, playwright: Playwright, user_credentials):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        user_email = user_credentials["user_email"]
        user_password = user_credentials["user_password"]
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": user_email, "userPassword": user_password})
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]

    def create_order(self, playwright: Playwright, user_credentials):
        access_token = self.get_access_token(playwright, user_credentials)
        print("access_token = ", access_token)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=orders_payload,
                                            headers={"Authorization": access_token,
                                                     "Content-Type": "application/json"
                                                     })
        print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id
