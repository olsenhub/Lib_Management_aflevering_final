from models.member import Member


class Library:
    """ 
    Management af bøger og lån. 
    Her kan vi tilføje, fjerne eller opdatere info om bøger. 
    Derudover tilføje, fjerne eller opdatere medlemmer(members).
    Man kan også låne bøger som medlem og returnerer bøger.
    Til sidst kan man se alle bøger og alle medlemmer samt søge på bøger(titel eller forfatter).
    """
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book) -> None:
        if book.item_id in self.books:
            raise ValueError("Book ID already exists.")
        self.books[book.item_id] = book

    def remove_book(self, book_id: str) -> None:
        if book_id not in self.books:
            raise ValueError("Book not found.")
        del self.books[book_id]

    def update_book(self, book_id: str, title=None, author=None, copies=None) -> None:
        if book_id not in self.books:
            raise ValueError("Book not found.")

        book = self.books[book_id]

        if title is not None:
            book.title = title
        if author is not None and hasattr(book, "author"):
            book.author = author
        if copies is not None and hasattr(book, "copies"):
            book.copies = copies

    def add_member(self, member: Member) -> None:
        if member.member_id in self.members:
            raise ValueError("Member ID already exists.")
        self.members[member.member_id] = member

    def remove_member(self, member_id: str) -> None:
        if member_id not in self.members:
            raise ValueError("Member not found.")
        del self.members[member_id]

    def update_member(self, member_id: str, name=None) -> None:
        if member_id not in self.members:
            raise ValueError("Member not found.")

        if name is not None:
            self.members[member_id].name = name

    def issue_book(self, member_id: str, book_id: str) -> None:
        if member_id not in self.members:
            raise ValueError("Member not found.")
        if book_id not in self.books:
            raise ValueError("Book not found.")

        book = self.books[book_id]
        member = self.members[member_id]

        if hasattr(book, "copies"):
            if book.copies <= 0:
                raise ValueError("No copies available.")
            book.copies -= 1

        member.borrow_book(book_id)

    def return_book(self, member_id: str, book_id: str) -> None:
        if member_id not in self.members:
            raise ValueError("Member not found.")
        if book_id not in self.books:
            raise ValueError("Book not found.")

        book = self.books[book_id]
        member = self.members[member_id]

        member.return_book(book_id)

        if hasattr(book, "copies"):
            book.copies += 1

    def display_books(self) -> None:
        if not self.books:
            print("No books in the library.")
            return

        for book in self.books.values():
            print(book.display_info())

    def display_members(self) -> None:
        if not self.members:
            print("No members in the library.")
            return

        for member in self.members.values():
            print(member.display_info())

    def search_books(self, keyword: str):
        keyword = keyword.lower()
        results = []

        for book in self.books.values():
            title_match = keyword in book.title.lower()
            author_match = hasattr(book, "author") and keyword in book.author.lower()

            if title_match or author_match:
                results.append(book)

        return results