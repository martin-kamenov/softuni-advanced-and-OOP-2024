from typing import List, Dict
from project.user import User

class Library:

    def __init__(self):
        self.user_records: List[User] = [] # [user1, user2,...]
        self.books_available: Dict[str: List[str]] = dict() # {author: [book1, book2, ...]}
        self.rented_books: Dict[str: Dict[str: int]] = dict() # {username: {book_name: days_to_return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books:
                self.rented_books[user.username] = {book_name: days_to_return}

            else:
                self.rented_books[user.username][book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for record in self.rented_books.values():
            if book_name in record:
                return f'The book "{book_name}" is already rented and will be available in {record[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str or None:
        if book_name not in self.rented_books[user.username]:
            return f"{user.username} doesn't have this book in his/her records!"

        del self.rented_books[user.username][book_name]
        user.books.remove(book_name)
        self.books_available[author].append(book_name)