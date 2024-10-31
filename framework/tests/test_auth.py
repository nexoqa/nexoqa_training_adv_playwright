# from playwright.sync_api import Page
# import pytest


# def test_auth(new_context, assert_snapshot):
#     page: Page = new_context(storage_state="./auth.json").new_page()
#     page.goto("http://ec2-3-249-201-236.eu-west-1.compute.amazonaws.com/")
#     assert_snapshot(page.screenshot(), threshold=0.1)


# @pytest.mark.only
# def test_auth2(new_context, assert_snapshot):
#     page: Page = new_context(storage_state="./auth.json").new_page()
#     page.goto("http://ec2-3-249-201-236.eu-west-1.compute.amazonaws.com/")
#     page.locator("div.song").nth(0)
#     assert_snapshot(
#         page.locator("div.song").nth(0).screenshot(), threshold=0.1, name="song1.png"
#     )
