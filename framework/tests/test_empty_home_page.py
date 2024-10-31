import pytest
from playwright.sync_api import Page, Route


from page_objects.home_page import HomePage


def test_empty_home_page(new_context):
    page: Page = new_context(storage_state="./auth.json").new_page()
    # clean_db.get(url="reset")
    page.route("**/songs", lambda route: route.fulfill(json={}))

    page.goto("http://ec2-3-249-201-236.eu-west-1.compute.amazonaws.com/")

    home_page: HomePage = HomePage(page)

    assert page.get_by_text("No slot content defined.").is_visible() == True


def test_only_two_songs(page: Page, clean_db):

    def handle(route: Route):
        route.fulfill(path="./data/resources/songs.json")

    clean_db.get(url="reset")

    page.route("**/songs", handle)

    page.goto("http://ec2-3-249-201-236.eu-west-1.compute.amazonaws.com/")

    home_page: HomePage = HomePage(page)

    page.wait_for_timeout(1000)

    assert len(page.locator("div.song").all()) == 2


def test_only_two_songs2(page: Page, clean_db):

    def handle(route: Route):
        response = route.fetch()
        json = response.json()
        new_songs = json[:2]
        route.fulfill(json=new_songs)

    clean_db.get(url="reset")

    page.route("**/songs", handle)

    page.goto("http://ec2-3-249-201-236.eu-west-1.compute.amazonaws.com/")

    home_page: HomePage = HomePage(page)

    page.wait_for_timeout(1000)

    assert len(page.locator("div.song").all()) == 2
