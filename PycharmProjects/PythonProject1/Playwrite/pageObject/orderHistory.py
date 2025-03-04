class OrderHistoryPage:
    def __init__(self,page):
        self.page = page

    def selectOrder(self,orderid):
        row = self.page.locator("tr").filter(has_text=orderid)  # finds the row in table and filters out the orderid
        row.get_by_role("button", name="View").click()
