class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            return True, book
        else:
            return False, None
        
    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            return True, book
        else:
            return False, None

    def view_borrowed_books(self):
        return self.borrowed_books

    def to_dict(self):
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": [book.isbn for book in self.borrowed_books]
        }



