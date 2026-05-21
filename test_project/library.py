from test_project.item import Item
from abc import ABC, abstractmethod
from test_project.book import Book
from test_project.magazine import Magazine

class Library:

    list_of_items = []

    def add_item(self, item):
         self.list_of_items.append(item)

    def list_all(self):
         for i in self.list_of_items:
            print(i)
    
    def borrow_item(item):
        Book.set_status(True)
    
    def return_item(item):
        Book.set_status(False)
        
    