import json
import pytest
from playwright.sync_api import Playwright
from utils.api_base import ApiUtils
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.orders_history import OrdersHistoryPage
from pages.order_details import OrderDetailsPage

# upload test data
with open('playwright/data/credentials.json') as file:
    credentials = json.load(file)
    print(credentials)
    user_credentials_list = credentials["user_credentials"]

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order -> orderId
    api_utils = ApiUtils()
    order_id = api_utils.create_order(playwright, user_credentials)

    # test data
    user_email = user_credentials["user_email"]
    user_password = user_credentials["user_password"]

    #login page
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(user_email, user_password)

    # dashboard page
    dashboard_page = DashboardPage(page)
    dashboard_page.open_orders_page()

    # orders page
    order_page = OrdersHistoryPage(page)
    order_page.select_order(order_id)

    # orders details page
    orders_details_page = OrderDetailsPage(page)
    orders_details_page.verify_order_message()
    context.close()

