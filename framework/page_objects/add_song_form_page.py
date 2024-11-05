from typing import Optional
from playwright.sync_api import Page


class AddSongFormPage:
    __page: Page

    def __init__(self, page: Page):
        self.__page = page

    def add_song(self):
        self.__page.locator("#sngBtn").click()
        self.__page.wait_for_selector("a[href='#/songs/create']")

    def fillSong(
        self,
        title: Optional[str],
        artist: Optional[str],
        genre: Optional[str],
        album: Optional[str],
        album_image: Optional[str],
        youtube_id: Optional[str],
        tab: Optional[str],
        lyrics: Optional[str],
    ):

        if title is not None:
            self.__page.locator("#sngTitle").fill(title)
        if artist is not None:
            self.__page.locator("#sngArtist").fill(artist)
        if genre is not None:
            self.__page.locator("#sngGenre").fill(genre)
        if album is not None:
            self.__page.locator("#sngAlbum").fill(album)
        if album_image is not None:
            self.__page.locator("#sngAlbumImg").fill(album_image)
        if youtube_id is not None:
            self.__page.locator("#sngYoutube").fill(youtube_id)
        if tab is not None:
            self.__page.locator("#sngTab").fill(tab)
        if lyrics is not None:
            self.__page.locator("#sngLyrics").fill(lyrics)
