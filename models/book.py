from models.lib_item import LibraryItem


class Book(LibraryItem):
    def __init__(self, item_id: str, title: str, author: str, copies: int):
        super().__init__(item_id, title)
        self.author = author
        self.copies = copies

    def display_info(self) -> str:
        return (
            f"[Book] ID: {self.item_id}, Title: {self.title}, "
            f"Author: {self.author}, Copies: {self.copies}"
        )