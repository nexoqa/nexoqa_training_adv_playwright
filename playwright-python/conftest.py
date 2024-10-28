from playwright.sync_api import Playwright, Browser, BrowserContext
import pytest

@pytest.fixture(scope='session', autouse=True)
def create_browser_context(playwright: Playwright):
    browser: Browser = playwright.chromium.launch()

    context: BrowserContext = browser.new_context()

    page = context.new_page()

    # Aquí va la sección de login

    context.storage_state(path='./my_session.json')

    context.close()