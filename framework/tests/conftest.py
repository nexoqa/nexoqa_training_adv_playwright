import time
from faker import Faker
import pytest

from data.song import Song
from playwright.sync_api import Playwright, Page


@pytest.fixture
def random_song() -> Song:
    return Song(
        title=Faker().name(),
        artist=Faker().name(),
        genre=Faker().name(),
        album=Faker().name(),
        album_image=(
            "https://is3-ssl.mzstatic.com/image/thumb/Features/d0/cc/62/dj.nanioukp.jpg/268x0w.jpg"
        ),
        youtube_id="WIUAC03YMlA",
        tab=Faker().text(),
        lyrics=Faker().text(),
    )


@pytest.fixture(scope="session")
def clean_db(playwright: Playwright):
    request_context = playwright.request.new_context(
        base_url="http://ec2-3-249-201-236.eu-west-1.compute.amazonaws.com:8081/"
    )
    yield request_context
    request_context.dispose()


@pytest.fixture(scope="session", autouse=True)
def login(browser, clean_db):
    clean_db.get("reset")
    page = browser.new_context().new_page()
    page.goto("http://ec2-3-249-201-236.eu-west-1.compute.amazonaws.com/#/register")
    page.locator("input[name='email']").fill("test@arsys.com")
    page.locator("input[name='password']").fill("12345678")
    page.get_by_role("button", name="Register").click()
    time.sleep(1)
    page.context.storage_state(path="auth.json")
    time.sleep(1)
    page.context.close()
