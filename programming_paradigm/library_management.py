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

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.__books.append(book)

    def  check_out_book(self, title):
        for book in self.__books:
            if book.title == title and book.check_cout():
                print(f"Checked out {book}")
                return
        print(f"Sorry, {title} in not not available")


    def return_book(self, title):
        for book in self.__books:
            if book.title == title and book.return_book():
                print(f"Returned: '{book}'")
                return
        print(f"Sorry '{title}' was checked out or does not exist.")


    def list_available_books(self):
        available_books = [book for book in self.__books if book.is_available()] 
        if available_books: 
            for book in available_books: 
                print(book)
        else: print("No books available.")