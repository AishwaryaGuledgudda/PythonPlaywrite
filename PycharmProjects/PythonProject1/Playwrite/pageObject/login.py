class loginPage:

#create a constructor
    def __init__(self, page):
        # self.page will have access to the entire class
        self.page = page #assigning the actual page object thats coming from test to local page object



#For this class to recognise "PAGE" , we have to create an object of this class in the actual method in test_webApi method

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self, userName,userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userName)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)
        self.page.locator("#login").click()