from playwright.sync_api import Page
import pytest


@pytest.mark.only
def test_auth(new_context):
    page: Page = new_context(storage_state="./auth.json").new_page()
    page.goto("http://ec2-63-35-198-228.eu-west-1.compute.amazonaws.com/")

    assert page.locator("#btn-logout").is_visible() == True
