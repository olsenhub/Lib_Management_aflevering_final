from models.book import Book
from models.member import Member
from models.library import Library


def test_add_book():
    library = Library()
    book = Book("B1", "test bog", "test forfatter", 3)

    library.add_book(book)

    assert "B1" in library.books
    assert library.books["B1"].title == "test bog"


def test_add_member():
    library = Library()
    member = Member("M1", "lucas")

    library.add_member(member)

    assert "M1" in library.members
    assert library.members["M1"].name == "lucas"


def test_issue_book():
    library = Library()
    book = Book("B1", "test bog", "test forfatter", 3)
    member = Member("M1", "lucas")

    library.add_book(book)
    library.add_member(member)
    library.issue_book("M1", "B1")

    assert "B1" in library.members["M1"].borrowed_books
    assert library.books["B1"].copies == 2


def test_return_book():
    library = Library()
    book = Book("B1", "test bog", "test forfatter", 3)
    member = Member("M1", "lucas")

    library.add_book(book)
    library.add_member(member)
    library.issue_book("M1", "B1")
    library.return_book("M1", "B1")

    assert "B1" not in library.members["M1"].borrowed_books
    assert library.books["B1"].copies == 3


def test_issue_book_no_copies():
    library = Library()
    book = Book("B1", "test bog", "test forfatter", 0)
    member = Member("M1", "lucas")

    library.add_book(book)
    library.add_member(member)

    try:
        library.issue_book("M1", "B1")
        assert False
    except ValueError as error:
        assert str(error) == "No copies available."


def test_return_book_not_borrowed():
    library = Library()
    book = Book("B1", "test bog", "test forfatter", 3)
    member = Member("M1", "lucas")

    library.add_book(book)
    library.add_member(member)

    try:
        library.return_book("M1", "B1")
        assert False
    except ValueError as error:
        assert str(error) == "This member has not borrowed that book."