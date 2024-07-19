from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content

class BaseFormatter(ABC):

    @abstractmethod
    def format(self, book: Book):
        ...


class PepperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:10]


class InstagramFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content


class FacebookFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:20]


class RandomFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f'@#$ {book.content} @##$'


class Printer:
    @staticmethod
    def get_book(book: Book, formatter: BaseFormatter):
        formatted_book = formatter.format(book)

        return formatted_book

book_ = Book('Some of the really long long content.')
printer = Printer()
print(printer.get_book(book_, FacebookFormatter()))
print(printer.get_book(book_, RandomFormatter()))