from faker import Faker
import pytest

from data.song import Song
from playwright.sync_api import Playwright


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
        base_url="http://ec2-18-203-244-192.eu-west-1.compute.amazonaws.com:8081/"
    )
    yield request_context
    request_context.dispose()
