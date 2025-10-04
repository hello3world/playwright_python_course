import time

from playwright.async_api import Page, expect

def intercept_request(route):
    route.continue_(url = "https://rahulshettyacademy.com/client/#/dashboard/order-details/68e11ae2559d6cb0afc7bd0")


def test_network(page: Page):
    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    # orders
    page.wait_for_url("**/client/**")
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)

