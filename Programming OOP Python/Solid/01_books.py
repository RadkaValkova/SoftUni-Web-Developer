class Book:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages


class Library:
    def __init__(self, location):
        self.location = location
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        try:
            book = [b for b in self.books if b.title == title][0]
            return f'Book {book} is found.'
        except:
            return 'Book not found.'


class Person:
    def __init__(self, name):
        self.name = name


class Reader(Person):
    def __init__(self, name, current_book):
        super().__init__(name)
        self.current_book = current_book
        self.current_page = 0

    def turn_page(self):
        self.current_page += 1
