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
   
   while True:
      print("Laba diena:")
      print("Programa leidžia atlikti sekančius veiksmus:")
      print("[1] - peržiūrėti visą sąrašą:")
      print("[2] - pasiskolinti knygą ar žurnalą")
      print("[3] - grąžinti knygą ar žurnalą")
      print("[4] - baigti progamą")
      selection = int(input("Įveskite jūsų pasirinkimą: "))
      if selection in range(1,5):
         if selection == 1:
            library_1.list_all()
         #==============================================
         if selection == 2:
            print("Norite pasiskolinti knygą[1] ar žurnalą[2]?")
            borrow_selection = int(input())
            if borrow_selection in range(1,3):
               if borrow_selection == 1:
                  print("Iveskite knygos antraštę:")
                  title = input()
                  print("Iveskite knygos autorių:")
                  author = input()
                  print("Iveskite knygos pavadinimą:")
                  name = input()
                  print("Iveskite knygos žanrą:")
                  genre = input()
                  if title != "" and author != "" and name != "" and genre != "":
                     library_1.borrow_item(Book(title, author, name, genre))
                  else:
                     print("Nebuvo įvesta viena iš reikšmių")
               if borrow_selection == 2:
                  print("Iveskite žurnalo antraštę:")
                  title = input()
                  print("Iveskite žurnalo autorių:")
                  author = input()
                  print("Iveskite žurnalo pavadinimą:")
                  name = input()
                  print("Iveskite žurnalo leidinio numerį:")
                  issue_id = input()
                  if title != "" and author != "" and name != "" and issue_id != "":
                     library_1.borrow_item(Magazine(title, author, name, issue_id))
                  else:
                     print("Nebuvo įvesta viena iš reikšmių")
            else:
               print("Neteisingai įvestas skaičius")  
         #======================================================
         if selection == 3:
            print("Norite grąžinti knygą[1] ar žurnalą[2]")
            return_selection = int(input())
            if return_selection in range(1,3):
               if return_selection == 1:
                  print("Iveskite knygos antraštę:")
                  title = input()
                  print("Iveskite knygos autorių:")
                  author = input()
                  print("Iveskite knygos pavadinimą:")
                  name = input()
                  print("Iveskite knygos žanrą:")
                  genre = input()
                  if title != "" and author != "" and name != "" and genre != "":
                     library_1.return_item(Book(title, author, name, genre))
                  else:
                     print("Nebuvo įvesta viena iš reikšmių")
               if return_selection == 2:
                  print("Iveskite žurnalo antraštę:")
                  title = input()
                  print("Iveskite žurnalo autorių:")
                  author = input()
                  print("Iveskite žurnalo pavadinimą:")
                  name = input()
                  print("Iveskite žurnalo leidinio numerį:")
                  issue_id = input()
                  if title != "" and author != "" and name != "" and issue_id != "":
                     library_1.return_item(Magazine(title, author, name, issue_id))
                  else:
                     print("Nebuvo įvesta viena iš reikšmių")
            else:
               print("Neteisingai įvestas skaičius")  

         if selection == 4:
            break
      else:
         print("Buvo neteisingai įvestas skaičius, pasirinkimas nuo 1 iki 4, kartokite")


    

if __name__ == "__main__":
    main() # funkcija yra paleidziama, tik kai main failas yra paleistas