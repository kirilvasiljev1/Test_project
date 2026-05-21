from test_project.item import Item
from abc import ABC, abstractmethod

class Book(Item):
    def __init__(self, title, author, name, genre):
        super().__init__(title, author, name)
        self.genre = genre
    
    @abstractmethod
    def get_details(self):
        return f"Book(Title: {self.title}, Author: {self.author}, Name: {self.name}, Genre: {self.genre})"
