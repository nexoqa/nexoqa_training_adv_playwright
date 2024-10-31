from faker import Faker
from playwright.sync_api import Page, expect


from page_objects.add_song_form_page import AddSongFormPage
from page_objects.home_page import HomePage


def test_add_new_song(page: Page, clean_db):
    response = clean_db.get(url="reset")

    title: str = Faker().name()
    artist: str = Faker().name()
    genre: str = Faker().name()
    album: str = Faker().name()
    album_image: str = (
        "https://is3-ssl.mzstatic.com/image/thumb/Features/d0/cc/62/dj.nanioukp.jpg/268x0w.jpg"
    )
    youtube_id: str = "WIUAC03YMlA"
    tab: str = Faker().text()
    lyrics: str = Faker().text()

    page.goto("http://ec2-3-249-201-236.eu-west-1.compute.amazonaws.com/")

    home_page: HomePage = HomePage(page)
    home_page.get_bt_add_song.click()
    add_new_page: AddSongFormPage = AddSongFormPage(page)
    add_new_page.fillSong(
        title=title,
        artist=artist,
        genre=genre,
        album=album,
        album_image=album_image,
        youtube_id=youtube_id,
        tab=tab,
        lyrics=lyrics,
    )
    add_new_page.add_song()

    

    assert page.get_by_text(title).is_visible() == True
