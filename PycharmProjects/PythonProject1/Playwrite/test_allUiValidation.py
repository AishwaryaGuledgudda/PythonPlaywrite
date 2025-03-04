import pytest
from playwright.sync_api import Page

@pytest.mark.smoke #when we give this command in terminal "pytest -m smoke" only methods with this comand will be excecuted
def test_textBoxVisible(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.get_by_placeholder("Hide/Show Example").is_visible() #Place holder is a new locator, this line checks if the text box is visible or no
    page.get_by_role("button", name="Hide").click()
    page.get_by_placeholder("Hide/Show Example").is_hidden()
    page.get_by_role("button", name="Show").click()
    page.get_by_placeholder("Hide/Show Example").is_visible()

def test_alertPopup(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog:dialog.accept()) #a listerner that listens if the pop up appears and then accepts it
    page.get_by_role("button", name="Confirm").click()

def test_switchFrames(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    secondFrame = page.frame_locator("#courses-iframe") #make sure to use frame locator inorder to locate a different frame on the page
    secondFrame.get_by_role("link", name="All Access plan").click()

def test_mouseHover(page:Page):
    page.locator("#mousehover").hover()
    #/Users/aishwaryaguledgudda/PycharmProjects/PythonProject1/Playwrite/test-results/test-alluivalidation-py-test-mousehover-chromium/trace.zip