class OrderDetailsPage:
    def __init__(self,page):
        self.page = page

    def verifyOrderMessage(self):
        viewtext = self.page.locator(".tagline").text_content()  # extracts the text from the view
        return viewtext
