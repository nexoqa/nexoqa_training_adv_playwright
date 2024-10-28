from playwright.sync_api import Page, Locator


class HomePage:
    page: Page

    def __init__(self, page: Page):
        self.page = page

    @property
    def get_bt_add_song(self) -> Locator:
        return self.page.locator("a[href='#/songs/create']")
    
    def get_view_song_by_title(self, title: str) -> Locator:
        return self.page.get_by_text(title).locator('../a')
