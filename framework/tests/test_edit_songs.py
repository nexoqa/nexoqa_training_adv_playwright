from playwright.sync_api import Page

from data.song import Song
from page_objects.home_page import HomePage
from page_objects.edit_song_form_page import EditSongFormPage
from page_objects.song_view_page import SongViewPage


def test_edit_song(page: Page, random_song: Song, clean_db):
    response = clean_db.get(url="reset")

    page.goto("http://ec2-18-203-244-192.eu-west-1.compute.amazonaws.com/")

    home_page: HomePage = HomePage(page)

    home_page.get_view_song_by_title("Nevermind").click()

    edit_song_page: SongViewPage = SongViewPage(page)

    edit_song_page.get_edit_button().click()

    song_form_page: EditSongFormPage = EditSongFormPage(page)

    song_form_page.fillSong(
        random_song.title,
        random_song.artist,
        random_song.genre,
        random_song.album,
        random_song.album_image,
        random_song.youtube_id,
        random_song.tab,
        random_song.lyrics,
    )

    song_form_page.modify_song()
    print(random_song.title)
    assert page.get_by_text(random_song.title).is_visible() == True
