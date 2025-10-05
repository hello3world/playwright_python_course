from .orders_history import OrdersHistoryPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def open_orders_page(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orders_page = OrdersHistoryPage(self.page)
        return orders_page
