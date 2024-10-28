import re
import pytest
from faker import Faker
from playwright.sync_api import Page, expect


def test_sign_up(page: Page):
    name: str = Faker().name()

    page.goto("https://automationexercise.com/")

    page.locator('button[aria-label="Consentir"]').click()

    page.locator('a[href="/login"]').click()
    page.locator('input[data-qa="signup-name"]').fill(name)
    page.locator('input[data-qa="signup-email"]').fill(Faker().email())

    page.locator('button[data-qa="signup-button"]').click()

    page.locator('input[data-qa="password"]').fill(Faker().password())
    page.locator('input[data-qa="first_name"]').fill(Faker().first_name())
    page.locator('input[data-qa="last_name"]').fill(Faker().last_name())
    page.locator('input[data-qa="address"]').fill(Faker().address())
    page.locator('input[data-qa="state"]').fill("Spain")
    page.locator('input[data-qa="city"]').fill("Logroño")
    page.locator('input[data-qa="zipcode"]').fill("00000")
    page.locator('input[data-qa="mobile_number"]').fill("666888777")

    page.locator('button[data-qa="create-account"]').click()

    assert page.locator('h2[data-qa="account-created"]').inner_text() == "ACCOUNT CREATED!"
    page.locator('a[data-qa="continue-button"]').click()

    assert page.locator("div.shop-menu ul li:last-child b").inner_text() == name

    page.locator('a[href="/delete_account"]').click()
    assert page.locator('h2[data-qa="account-deleted"]').inner_text() == "ACCOUNT DELETED!"
