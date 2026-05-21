from abc import abstractmethod

from test_project.item import Item

class Magazine(Item):
    def __init__(self, title, author, name, issue_number):
        super().__init__(title, author, name)
        self.issue_number = issue_number
    
    @abstractmethod
    def get_details(self):
        return f"Book(Title: {self.title}, Author: {self.author}, Name: {self.name}, Genre: {self.issue_number})"