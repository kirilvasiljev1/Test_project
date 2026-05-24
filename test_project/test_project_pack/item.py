from abc import ABC, abstractmethod

class Item(ABC):
    
    def __init__(self, title, author, name):
        super().__init__()
        self.title = title
        self.author = author
        self.name = name
        self.__is_checked_out = False
        
    @property # getter
    def is_checked_out(self):
        return self.__is_checked_out
    
    @is_checked_out.setter
    def is_checked_out(self, __is_checked_out):
        self.__is_checked_out = __is_checked_out
    
    @abstractmethod
    def get_details(self):
        ...

    