from member import Member
from book import Book
import json, os


# Build the path to library_data.json relative to this file.
# This means the program can find the data file regardless of
# where the application is launched from.
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "library_data.json")


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books[isbn] = new_book
        return new_book

    def register_member(self, name, member_id):
        new_member = Member(name, member_id)
        self.members[member_id] = new_member
        return new_member

    def find_book(self, isbn):
        if isbn in self.books:
            return True, self.books[isbn]
        else:
            return False, None

    def find_book_by_title(self, title):
        for book in self.books.values():
            if title == book.title:
                return book
        return None

    def find_member(self, member_id):
        if member_id in self.members:
            return self.members[member_id]
        else:
            return None

    def get_available_books(self):
        available_books = []

        for isbn, book in self.books.items():
            if book.available:
                available_books.append(book)

        return available_books

    def get_all_books(self):
        books = []

        for isbn, book in self.books.items():
            books.append(book)

        return books

    def get_members(self):
        members = []

        for member_id, member in self.members.items():
            members.append(member)

        return members

    def remove_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            del self.books[isbn]
            return True, book
        else:
            return False, None

    def save_data(self):
        # Convert the Book and Member objects into dictionaries
        # so they can be stored as JSON.
        data = {
            "books": {},
            "members": {}
        }

        for isbn, book in self.books.items():
            data["books"][isbn] = book.to_dict()

        for member_id, member in self.members.items():
            data["members"][member_id] = member.to_dict()

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        # JSON cannot store Python objects directly, so the saved
        # dictionaries are converted back into Book and Member objects.
        with open(file_path, "r") as f:
            data = json.load(f)

        # Recreate all Book objects from the saved data.
        for isbn, info in data["books"].items():

            book = Book(
                info["title"],
                info["author"],
                info["isbn"]
            )

            book.available = info["available"]

            self.books[isbn] = book

        # Recreate all Member objects and restore their borrowed books.
        for member_id, info in data["members"].items():

            member = Member(
                info["name"],
                info["member_id"]
            )

            # borrowed_books contains ISBNs in the JSON file.
            # Convert each ISBN back into the corresponding Book object.
            for isbn in info["borrowed_books"]:

                if isbn in self.books:
                    book = self.books[isbn]
                    member.borrowed_books.append(book)

            self.members[member_id] = member