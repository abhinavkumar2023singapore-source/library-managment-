# inventory.py
import json
from pathlib import Path
import numpy as np
from book import Book


class LibraryInventory:
    """
    LibraryInventory manages multiple book objects.
    Demonstrates:
    - Abstraction (easy methods to manage books)
    - Encapsulation (list stored internally)
    """

    def __init__(self, file_path="books.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_books()

    # ----------------------- File Handling -----------------------
    def load_books(self):
        """Load books from JSON into object form."""
        try:
            if self.file_path.exists():
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    for b in data:
                        self.books.append(Book(**b))
        except Exception:
            print("Error: Could not read JSON file.")

    def save_books(self):
        """Save all books to JSON file."""
        try:
            data = [b.to_dict() for b in self.books]
            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=4)
        except Exception:
            print("Error: Could not save file.")

    # ----------------------- Core Operations -----------------------
    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        if not self.books:
            print("No books in inventory.")
            return
        for book in self.books:
            print(book)

    # ----------------------- Small Numpy Feature -----------------------
    def inventory_stats(self):
        """Simple statistics using numpy."""
        if not self.books:
            return {"total": 0, "available": 0, "issued": 0}

        statuses = np.array([b.to_dict()["status"] for b in self.books])

        return {
            "total": len(self.books),
            "available": int((statuses == "available").sum()),
            "issued": int((statuses == "issued").sum())
        }
