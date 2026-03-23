from models.lib_item import LibraryItem
"""
SE 'book.py' FOR DOKUMENTATION. Samme koncept her
"""

class EBook(LibraryItem):
    def __init__(self, item_id: str, title: str, author: str, file_size_mb: float):
        super().__init__(item_id, title)
        self.author = author
        self.file_size_mb = file_size_mb

    def display_info(self) -> str:
        return (
            f"[EBook] ID: {self.item_id}, Title: {self.title}, "
            f"Author: {self.author}, Size: {self.file_size_mb} MB"
        )