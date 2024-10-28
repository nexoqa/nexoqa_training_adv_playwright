from typing import Optional
from playwright.sync_api import Page, Locator


class EditSongFormPage:
    __page: Page

    def __init__(self, page: Page):
        self.__page = page

    def modify_song(self):
        self.__page.get_by_text("Save Song").click()
        self.__page.wait_for_timeout(1000)

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
        self.__page.wait_for_timeout(1000)
        if title is not None:
            self.__page.locator("input[aria-label='Title']").fill(title)
        if artist is not None:
            self.__page.locator("input[aria-label='Artist']").fill(artist)
        if genre is not None:
            self.__page.locator("input[aria-label='Genre']").fill(genre)
        if album is not None:
            self.__page.locator("input[aria-label='Album']").fill(album)
        if album_image is not None:
            self.__page.locator("input[aria-label='Album Image Url']").fill(album_image)
        if youtube_id is not None:
            self.__page.locator("input[aria-label='YouTube ID']").fill(youtube_id)
        if tab is not None:
            self.__page.locator("textarea[aria-label='Tab']").fill(tab)
        if lyrics is not None:
            self.__page.locator("textarea[aria-label='Lyrics']").fill(lyrics)
