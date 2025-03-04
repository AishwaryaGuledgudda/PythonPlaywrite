import json

import pytest
from playwright.sync_api import Playwright, expect

from pageObject.orderDetails import OrderDetailsPage
from pageObject.dashboard_home import DashboardHome
from pageObject.orderHistory import OrderHistoryPage
from pageObject.login import loginPage
from utils.apiBase import APIUtils

# json file -->util-->access into test
with open('data/credentials.json') as f:
    test_data = json.load(f)  # load is a method that will convert json file to python object
    print(test_data)
    credent_list = test_data['user_credentials']


#when we use parameterize it extracts single data/creds from the list (credent_list) and excecutes the code for that creds
#when the method extracts the first data it gets stored in user_cred
@pytest.mark.parametrize('user_cred_fixture', credent_list)
def test_webApi(playwright: Playwright, user_cred_fixture):
    #user_cred_fixture should return the user_cred values for test_webApi method to use the data to parameterize
    #use a global file Conftest to write fixture , so this fixture should return the params declared in this method
    userName = user_cred_fixture["user_id"] #creating these two variables so that we can pass it as arguments in login_page.login method
    userPassword = user_cred_fixture["Password"]
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order using API in a new class
    api_utils = APIUtils()
    orderid = api_utils.placeOrder(playwright, user_cred_fixture)  #ustils also has username and password hard code data
    #hence add user_cred_fixture as parameter to send along wth playwright

    #login using UI
    login_Page = loginPage(page) #creating object of the class loginpage and passing "PAGE" argument
    login_Page.navigate() #This step covers the {page.goto("https://rahulshettyacademy.com/client")} step
    #page.goto("https://rahulshettyacademy.com/client") this step is no longer needed as we used the above code
    login_Page.login(userName,userPassword)
    '''the above is a framework method call for all the below three lines, sending two arguments because we are extracting
     those two variables from the "Credentials.json" file and if we do not send as arguments they throw error in the login class {user_cred_fixture["user_id"]} these two lines'''
    #page.get_by_placeholder("email@example.com").fill(user_cred_fixture["user_id"])
    #page.get_by_placeholder("enter your passsword").fill(user_cred_fixture["Password"])
    #page.locator("#login").click()

    dashboard_home = DashboardHome(page) #creating object of the new Dashboard home class to access all the methods in it
    dashboard_home.selectOrderNavigation() #calling the selectOrderNavigation() using the created object as it is in different class we do not need the below code line
    #page.get_by_role("button", name="  ORDERS").click()

    order_history = OrderHistoryPage(page)
    order_history.selectOrder(orderid) #sending orderID as parameter
    #row = page.locator("tr").filter(has_text=orderid)  #finds the row in table and filters out the orderid
    #row.get_by_role("button", name="View").click()  #goes inside that row to look for view button and click on it
    order_details = OrderDetailsPage(page)
    view_text = order_details.verifyOrderMessage() # calling verifyOrderMessage method by creating object of that class this line replaces the below lin eof code
    #creating "view_text" variable so that the extraceted text is returned and caught in it
    #viewtext = page.locator(".tagline").text_content()  #extracts the text from the view
    assert view_text  #verifies the text
    # expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")  #to_have_text exactly matches the text exactly, to_contain_text partially matchs the text
    print(view_text)
