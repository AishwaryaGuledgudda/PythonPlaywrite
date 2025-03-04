from playwright.sync_api import Playwright

ordPayloadData = {"orders":[{"country": "India","productOrderedId": "67a8df1ac0d3e6622a297ccb"}]}

class APIUtils:

    def getToken(self, playwright: Playwright, user_cred_fixture):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url= "/api/ecom/auth/login", data={"userEmail":user_cred_fixture["user_id"],"userPassword":user_cred_fixture["Password"]})
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def placeOrder(self, playwright: Playwright, user_cred_fixture):
        token = self.getToken(playwright,user_cred_fixture) #sending user_cred_fixture as parameter as the username and password is in that method
        api_request_context = playwright.request.new_context( base_url= "https://rahulshettyacademy.com")
        response = api_request_context.post(url="api/ecom/order/create-order", data=ordPayloadData, headers={"Authorization": token, "Content-Type":"application/json"})
        print(response.json())
        response = response.json()
        order_id = response["orders"][0]
        print(order_id)
        return order_id
