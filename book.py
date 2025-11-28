#abhinav kumar 2501350050
# book.py
class Book:
    """
    Book class represents a single book item in the library.
    Demonstrates:
    - Encapsulation: internal status control
    - Abstraction: simple methods for issuing/returning
    """

    def __init__(self, title, author, isbn, status="available"):
        # Attributes
        self.title = title
        self.author = author
        self.isbn = isbn
        self._status = status      # Encapsulated (treated as private)

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {self._status}"

    # ---- Abstraction: Public methods hide internal working ----
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self._status
        }

    def issue(self):
        """Issue book only if available."""
        if self._status == "available":
            self._status = "issued"
            return True
        return False

    def return_book(self):
        """Return book only if it was issued."""
        if self._status == "issued":
            self._status = "available"
            return True
        return False

    def is_available(self):
        return self._status == "available"

