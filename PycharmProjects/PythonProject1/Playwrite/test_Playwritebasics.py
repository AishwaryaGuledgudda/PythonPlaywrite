import time

from playwright.sync_api import Page, expect


def test_browserLaunch(playwright):
    browser= playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page= context.new_page()
    page.goto("https://www.google.com")

def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    #Below code is to validate the alert textbox when entered wrong creds
    #expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)
