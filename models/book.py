from models.lib_item import LibraryItem


class Book(LibraryItem):
    """
    Den her klasse er for bøger
    """
    def __init__(self, item_id: str, title: str, author: str, copies: int):
        """
        Her initialiseres den nye bog
        ID = string for bogens unikke ID
        Title = bogens titel
        Author = bogens forfatter
        Copies = antal kopier
        """
        super().__init__(item_id, title)
        self.author = author
        self.copies = copies
        

    def display_info(self) -> str:
        """
        Return giver en string med info om bogen
        """
        return (
            f"[Book] ID: {self.item_id}, Title: {self.title}, "
            f"Author: {self.author}, Copies: {self.copies}"
        )