class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self.__is_checked_out

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.check_out():
                print(f"Checked out {book}")
                return
        print(f"Sorry, {title} is not available")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.return_book():
                print(f"Returned: '{book}'")
                return
        print(f"Sorry, '{title}' was not checked out or does not exist.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")
