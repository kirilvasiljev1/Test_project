from abc import ABC, abstractmethod

from test_project_pack.item import Item
from test_project_pack.book import Book
from test_project_pack.magazine import Magazine

class Library():

    list_of_items = []

    def add_item(self, entry):
        self.list_of_items.append(entry)

    def list_all(self):
        for i in self.list_of_items:
            print(i.get_details(), i.is_checked_out)

    def borrow_item(self, entry):
        for item in self.list_of_items:
            if item.get_details() == entry.get_details() and item.is_checked_out == False:
               item.is_checked_out = True
            elif item.get_details() == entry.get_details() and item.is_checked_out == True:
                print("Sorry item: \n", item.get_details(), "\n is already borrowed \n")
                
    def return_item(self, entry):
        for item in self.list_of_items:
            if item.get_details() == entry.get_details() and item.is_checked_out == True:
               item.is_checked_out = False
            elif item.get_details() == entry.get_details() and item.is_checked_out == False:
                print("Sorry item: ", item.get_details(), " is already has been returned")
