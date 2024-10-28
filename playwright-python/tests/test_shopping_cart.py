import re
import pytest
from playwright.sync_api import Page, expect

def test_add_item_to_shopping_cartp(page: Page):
    page.goto("https://automationexercise.com/")

    # cookies
    page.locator('button[aria-label="Consentir"]').click()

    #
    page.locator('div.shop-menu a[href="/view_cart"]').click()
    page.locator('#empty_cart > p > a[href="/products"]').click()
    page.locator('div.single-products').nth(0).hover()

    page.locator('div.single-products').nth(0).locator('.overlay-content > .btn.btn-default.add-to-cart').click()
    page.locator('div.shop-menu a[href="/view_cart"]').click()
    assert len(page.locator('#cart_info_table > tbody > tr').all()) == 1
