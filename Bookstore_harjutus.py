class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author, price, and rating.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        :param rating: book's rating
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor. Each book store has a name and a rating. 
        The store also manages a list of books.

        :param name: book store name
        :param rating: store's rating
        """
        self.name = name
        self.rating = rating
        self.books = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if the book can be added.

        It is possible to add a book if:
        1. The book with the same author and title is not already present in the store.
        2. The book's rating is greater than or equal to the store's rating.

        :return: bool
        """
        # Check if a book with the same title and author already exists
        for existing_book in self.books:
            if existing_book.title == book.title and existing_book.author == book.author:
                return False
        # Check if the book's rating is greater than or equal to the store's rating
        if book.rating < self.rating:
            return False
        return True

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):
            self.books.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if a book can be removed from the store.

        A book can be removed if it is present in the store.

        :return: bool
        """
        return book in self.books

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if self.can_remove_book(book):
            self.books.remove(book)

    def get_all_books(self) -> list:
        """
        Return a list of all books in the current store.

        :return: list of Book objects
        """
        return self.books

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        return sorted(self.books, key=lambda book: book.price)

    def get_most_popular_book(self) -> list:
        """
        Return a list of book(s) with the highest rating.

        :return: list of Book objects
        """
        if not self.books:
            return []
        max_rating = max(book.rating for book in self.books)
        return [book for book in self.books if book.rating == max_rating]
