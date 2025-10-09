import pytest
import json
from playwright.sync_api import Playwright, expect
from utils.api_base import ApiUtils

# upload test data
with open("playwright/data/credentials.json") as file:
    credentials = json.load(file)
    print(credentials)
    user_credentials_list = credentials["user_credentials"]

@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_session_storage(playwright: Playwright, user_credentials):
    api_utils = ApiUtils()
    get_token = api_utils.get_access_token(playwright, user_credentials)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f'''
    localStorage.setItem("token", "{get_token}")
    ''')
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/myorders")
    expect(page.get_by_text('Your Orders')).to_be_visible()