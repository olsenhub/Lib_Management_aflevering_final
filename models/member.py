class Member:
    """
    Den her klasse er for members - medlemmer

    ID = Unikt ID for medlem
    navn = navn
    borrowed_books = lånte bøger med ID vist
    history = låne og returnerings historik
    """
    def __init__(self, member_id: str, name: str):
        """
        Initialiserer et nyt medlem
        """
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        self.history = []

    def display_info(self) -> str:
        return (
            f"Member ID: {self.member_id}, Name: {self.name}, "
            f"Borrowed books: {self.borrowed_books}"
        )

    def borrow_book(self, book_id: str) -> None:
        self.borrowed_books.append(book_id)
        self.history.append(f"Borrowed {book_id}")

    def return_book(self, book_id: str) -> None:
        if book_id not in self.borrowed_books:
            raise ValueError("This member has not borrowed that book.")

        self.borrowed_books.remove(book_id)
        self.history.append(f"Returned {book_id}")