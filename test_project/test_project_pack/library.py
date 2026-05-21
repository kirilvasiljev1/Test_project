from abc import ABC, abstractmethod

from test_project_pack.item import Item
from test_project_pack.book import Book
from test_project_pack.magazine import Magazine

class Library:

    list_of_items = {}

    def add_item(self,item):
         self.take = Item()
         self.list_of_items[item] = self.take.set_status(True)

    def list_all(self):
        for i in self.list_of_items:
            i.get_details(), print(self.list_of_items[i])

            #if isinstance(i, Book):
            #    i.get_details()
            #if isinstance(i, Magazine):
            #    i.get_details()
    
             
            

    
    
    def borrow_item(item):
        Item.set_status(True)
    
    def return_item(item):
        Item.set_status(False)
        
    