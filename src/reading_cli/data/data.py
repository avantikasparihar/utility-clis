from abc import ABC, abstractmethod

class Book:
    def __init__(self, id, title, total_pages, percent_finished_prev, percent_finished_now):
        self.id = id
        self.title = title
        self.total_pages = total_pages
        self.percent_finished_prev = percent_finished_prev
        self.percent_finished_now = percent_finished_now

class BooksManager(ABC):
    @abstractmethod
    def get_book(self, id):
        pass

    @abstractmethod
    def list_books(self):
        pass

    @abstractmethod
    def create_book(self, new_book):
        pass

    @abstractmethod
    def update_book(self, updated_book):
        pass

    @abstractmethod
    def delete_book(self, id):
        pass