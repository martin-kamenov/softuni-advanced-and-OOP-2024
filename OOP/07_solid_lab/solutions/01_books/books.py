from typing import List


class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:

    def __init__(self):
        self.books: List = []

    def add_book(self, book: Book) -> str:
        if book not in self.books:
            self.books.append(book)

        return f'Book {book.title} added to the library.'

    def find_book(self, title: str) -> str:
        try:
            book = next((b for b in self.books if b.title == title))
            return f'Book {book.title} is in library.'
        except StopIteration:
            return f'Sorry, book {title} is not in library.'

    def remove_book(self, title: str) -> str:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)

                return f'Book {title} successfully removed from library.'

book1 = Book('Lord of the Rings', 'J. R. R. Tolkien')
book2 = Book('Harry Potter and a Half Blood Prince', 'J. K. Rowling')

library = Library()
library.add_book(book1)
print(', '.join(b.title for b in library.books))
library.add_book(book2)
print(', '.join(b.title for b in library.books))

print()

print(library.find_book('Lord of the Rings'))

print(library.remove_book('Lord of the Rings'))
print()
print(', '.join(b.title for b in library.books))


