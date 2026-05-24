from abc import abstractmethod

from test_project_pack.item import Item

class Magazine(Item):
    def __init__(self, title, author, name, issue_number):
        super().__init__(title, author, name)
        self.issue_number = issue_number
    

    def get_details(self):
        return f"Magazine(Title: {self.title}, Author: {self.author}, Name: {self.name}, Issue_number: {self.issue_number})"