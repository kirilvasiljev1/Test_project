from abc import ABC, abstractmethod
from test_project_pack import Item
from test_project_pack import Book
from test_project_pack import Magazine
from test_project_pack import Library

library_1 = Library()
book_1 = Book("Title 1", "Author 1", "Name 1", "Fantasy 1")
book_2 = Book("Title 2", "Author 2", "Name 2", "Fantasy 2")

magazine_1 = Magazine("Modo","Any Author", "Aliens", "2026.12.12")
magazine_2 = Magazine("Modo2","Any Author2", "Aliens2", "2026.11.11")

def main():
   library_1.add_item(book_1)
   library_1.add_item(magazine_1)
   library_1.add_item(book_2)
   library_1.add_item(magazine_2)
   library_1.list_all()
   library_1.borrow_item(book_1)
   library_1.list_all()
   library_1.borrow_item(book_1)




    

if __name__ == "__main__":
    main() # funkcija yra paleidziama, tik kai main failas yra paleistas