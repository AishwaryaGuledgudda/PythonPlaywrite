from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_webApi(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order using API in a new class
    api_utils = APIUtils()
    orderid = api_utils.placeOrder(playwright)

    #login using UI
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("aishwaryabg.abg@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Qwerty@123456")
    page.locator("#login").click()


    #order history page --> verify if the order is present
    page.get_by_role("button", name="  ORDERS").click()
    row = page.locator("tr").filter(has_text= orderid) #finds the row in table and filters out the orderid
    row.get_by_role("button", name= "View").click() #goes inside that row to look for view button and click on it
    viewtext = page.locator(".tagline").text_content() #extracts the text from the view
    assert viewtext #verifies the text
    # expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")  #to_have_text exactly matches the text exactly, to_contain_text partially matchs the text
    print(viewtext)