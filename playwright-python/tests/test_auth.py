from playwright.sync_api import Page

def test_auth(new_context):
    page: Page = new_context(storage_state="./auth.json").new_page()
    page.goto('https://automationexercise.com/')
    
    page.pause()
