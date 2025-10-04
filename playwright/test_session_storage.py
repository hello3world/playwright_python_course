from playwright.async_api import Playwright, expect
from utils.api_base import ApiUtils


def test_session_storage(playwright: Playwright):
    api_utils = ApiUtils()
    get_token = api_utils.get_access_token(playwright)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script('''
    localStorage.setItem("token", "{get_token}")
    ''')
    page.goto("https://rahulshettyacademy.com/client/")
    expect(page.get_by_text('Your Orders')).to_be_visible()