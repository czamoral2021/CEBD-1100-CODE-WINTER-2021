import sys
from termcolor import colored, cprint
#
# text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
# print(text)
# cprint('Hello, World!', 'green', 'on_red')

class Book:

    def __init__(self, ISBN, title, used):
        self.ISBN = ISBN
        self.title = title
        self.owner = "Biblioteque Brossard"
        self.used = used

    def is_book_used(self):
        return self.used



book1 = Book("123456789", "War of the Worlds", False)

book1.title = "Some other title"

book2 = Book("234567890", "Insomnia", False)
book3 = Book(None, "Insomnia Part 2", True)
array_of_books = [book1, book2, book3]

for b in array_of_books:
    print(b.title)
    print("Book used?", end="")
    if b.is_book_used():
        cprint("YES", color="red", on_color="on_yellow")
    else:
        cprint("NO", color="blue")