import time

from playwright.async_api import Page, expect

fakePayloadOrderResponse = {"message":"No Product in Cart"}

def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )


def test_network(page: Page):
    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/user/get-cart-count/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    # orders
    page.wait_for_url("**/client/**")
    page.get_by_role("button", name="ORDERS").click()
    order = page.locator(".mt-4")
    order.wait_for(state="visible")
