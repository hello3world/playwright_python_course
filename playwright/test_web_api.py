from playwright.sync_api import Playwright, expect

from utils.api_base_without_parametrize import ApiUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    #create order -> orderId
    api_utils = ApiUtils()
    order_id = api_utils.create_order(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("e.pavlovich29@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("1478963148635Jane*")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()

    #orders History page-> order is present.
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()

