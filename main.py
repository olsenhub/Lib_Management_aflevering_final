from models.book import Book
from models.ebook import EBook
from models.member import Member
from models.library import Library


def show_menu():
    print("\nOlsens Library Management Services")
    print("1. Add Book")
    print("2. Add EBook")
    print("3. Add Member")
    print("4. Remove Book")
    print("5. Remove Member")
    print("6. Update Book")
    print("7. Update Member")
    print("8. Issue Book")
    print("9. Return Book")
    print("10. Display Books")
    print("11. Display Members")
    print("12. Search Books")
    print("13. Exit")


def main():
    library = Library()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                item_id = input("Book ID: ")
                title = input("Title: ")
                author = input("Author: ")
                copies = int(input("Copies: "))

                book = Book(item_id, title, author, copies)
                library.add_book(book)
                print("Book added successfully.")

            elif choice == "2":
                item_id = input("EBook ID: ")
                title = input("Title: ")
                author = input("Author: ")
                file_size_mb = float(input("File size in MB: "))

                ebook = EBook(item_id, title, author, file_size_mb)
                library.add_book(ebook)
                print("EBook added successfully.")

            elif choice == "3":
                member_id = input("Member ID: ")
                name = input("Member name: ")

                member = Member(member_id, name)
                library.add_member(member)
                print("Member added successfully.")

            elif choice == "4":
                book_id = input("Book ID to remove: ")
                library.remove_book(book_id)
                print("Book removed successfully.")

            elif choice == "5":
                member_id = input("Member ID to remove: ")
                library.remove_member(member_id)
                print("Member removed successfully.")

            elif choice == "6":
                book_id = input("Book ID to update: ")
                title = input("New title (leave blank to skip): ")
                author = input("New author (leave blank to skip): ")
                copies_input = input("New copies (leave blank to skip): ")

                title = title if title else None
                author = author if author else None
                copies = int(copies_input) if copies_input else None

                library.update_book(book_id, title=title, author=author, copies=copies)
                print("Book updated successfully.")

            elif choice == "7":
                member_id = input("Member ID to update: ")
                name = input("New name (leave blank to skip): ")
                name = name if name else None

                library.update_member(member_id, name=name)
                print("Member updated successfully.")

            elif choice == "8":
                member_id = input("Member ID: ")
                book_id = input("Book ID: ")

                library.issue_book(member_id, book_id)
                print("Book issued successfully.")

            elif choice == "9":
                member_id = input("Member ID: ")
                book_id = input("Book ID: ")

                library.return_book(member_id, book_id)
                print("Book returned successfully.")

            elif choice == "10":
                library.display_books()

            elif choice == "11":
                library.display_members()

            elif choice == "12":
                keyword = input("Search by title or author: ")
                results = library.search_books(keyword)

                if not results:
                    print("No matching books found.")
                else:
                    for item in results:
                        print(item.display_info())

            elif choice == "13":
                print("Goodbye.")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()