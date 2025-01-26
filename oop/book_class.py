class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Modify to print the title instead of the year
        print(f"Deleting {self.title}")

    def __str__(self):
        # Ensure this returns the "Book(...)" format
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Ensure this returns the "1984 by George Orwell, published in 1949" format
        return f"Book('{self.title}', '{self.author}', {self.year})"
