from playwright.sync_api import Page, Locator

class SongViewPage:
    def __init__(self, page: Page) -> None:
        self.__page = page

    def get_edit_button(self) -> Locator:
        return self.__page.get_by_text("Edit")
    