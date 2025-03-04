from playwright.sync_api import Page, expect


def test_uiAddtoCart(page:Page):
    #Add iphoneX and Nokia Edge --> verify 2 items are added in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphonex = page.locator("app-card").filter(has_text="iphone X")
    iphonex.get_by_role("button", name="Add ").click()
    nokia = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-object")).to_have_count(2)

#clicks on blinking link , on new page it picks up the red test and splits the text in to many parts
# and compares it with the email and prints the email
def test_childWindow(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info :
        page.locator(".blinkingText").click()
        childPage = newPage_info.value
        textcontent = childPage.locator(".im-para.red").text_content()
        content = textcontent.split("at") #['Please email us',' mentor@rahulshettyacademy.com with below template to receive response']
        email = content[1].strip().split(" ") # removes white spaces befpre email id ['mentor@rahulshettyacademy.com' , 'with', 'below', 'template','to' , 'receive' ]
        assert email[0] == "mentor@rahulshettyacademy.com" # [mentor@rahulshettyacademy.com]
        print(email[0]) # mentor@rahulshettyacademy.com


