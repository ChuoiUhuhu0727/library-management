class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Librarian:
    def __init__(self, library):
        self.library = library

    def add_book(self, title, author, isbn):
        self.library.books_data.append(Book(title, author, isbn))

    def remove_book(self, title):
        before = len(self.library.books_data)
        self.library.books_data = [book for book in self.library.books_data if book.title.lower() != title.lower()]
        after = len(self.library.books_data)
        if before == after:
            raise ValueError("Book not found.")

class Member:
    def __init__(self, name, member_type):
        self.name = name
        self.member_type = member_type.lower()
        self.books = []

    def borrow_book(self, book_title):
        self.count_books()
        self.books.append(book_title)
        return f"{self.name} successfully borrows {book_title}"

    def count_books(self):
        count_books = len(self.books)
        if self.member_type == "regular" and count_books >= 3:
            raise Exception("You can't borrow more than 3 books")
        elif self.member_type == "premium" and count_books >= 5:
            raise Exception("You can't borrow more than 5 books")
        return count_books

class Library:
    def __init__(self, books_data, members_data):
        self.books_data = [Book(b["title"], b["author"], b["isbn"]) for b in books_data]
        self.members_data = [Member(m["name"], m["member_type"]) for m in members_data]

    def check_role(self, input_role, input_name):
        if input_role in ("regular", "premium"):
            user = self.check_name(input_name)
            if user: return
            else: raise ValueError("Your name doesn't exist")
        else:
            raise ValueError("Your role doesn't exist")

    def check_name(self, input_name):
        for mem in self.members_data:
            if input_name == mem.name:
                return mem
        raise ValueError("Your name doesn't exist")

    def check_action(self, input_action):
        if input_action in ("borrow", "return"):
            return
        else:
            raise ValueError("Your action doesn't exist")

    def check_book(self, user, input_action, input_book):
        for book in self.books_data:
            if input_book.lower() == book.title.lower():
                return user.borrow_book(input_book)
        raise ValueError("Your book doesn't exist")