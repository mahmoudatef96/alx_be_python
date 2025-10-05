class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def get_status(self):
        """Returns the current availability status of the book."""
        return "Checked Out" if self._is_checked_out else "Available"

    def __str__(self):
        """String representation of the book."""
        return f"'{self.title}' by {self.author} ({self.get_status()})"
    def return_book(self, title):
        for book in self._books:
            if book.title.lower == title.lower:
                if book._is_checked_out:
                    book._is_checked_out = False
                    return book.title
    def check_out_book(self, title):
        for book in self._books:
            if title == book.title:
                book._is_checked_out = True
                break


class Library:
    def __init__(self):
         self._books = []

    def add_book (self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if title == book.title:
                book._is_checked_out = True
                break
    def return_book(self, title):
        for book in self._books:
            if book.title.lower == title.lower:
                if book._is_checked_out:
                    book._is_checked_out = False
                    return book.title
    def list_available_books(self):
        available = [book for book in self._books if not book._is_checked_out]
        for book in available:
                print(book)