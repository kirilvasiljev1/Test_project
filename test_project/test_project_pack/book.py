from abc import ABC, abstractmethod

from test_project_pack.item import Item

class Book(Item):
    def __init__(self, title, author, name, genre):
        super().__init__(title, author, name)
        self.genre = genre
    
    def get_details(self):
        print (f"Book(Title: {self.title}, Author: {self.author}, Name: {self.name}, Genre: {self.genre})")
