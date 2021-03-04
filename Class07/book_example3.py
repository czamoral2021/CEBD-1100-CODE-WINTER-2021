class Book:
    # constructor function in OOP - Object-oriented programming
    def __init__(self, ISBN, title, used):
        self._ISBN = ISBN
        self._title = title
        self._owner = "Biblioteque Brossard"
        self. used = used
    # _ underscore means private, you cannot assign values directly

    # def set_isbn(self, isbn_value):
    #         self.ISBN = isbn_value
    # SET should be forbidden FOR isbn, because it is a key of the object not possible to change once it is created

    def get_isbn(self):
        return self._ISBN

    # GETTER BUT NOT SETTER => read only

    def set_title(self, title):
        self._title = title

    def get_title(self):
        return self._title



book1 = Book("123456789", "War of the Worlds", False)

book1.set_title("Some other title")

# book2 = Book("23456789", "Insomnia", False)
# book3 = Book(None, "Insomnia Part 2", True)
# # This book is in hold , not available, please do not create it in the DB
#
# # print(book2.title)
# array_of_books = [book1, book2, book3]
#
# # for b in array_of_books:
# #     print(b.title)
# #     print("Book used", end="")
# #     if b.is_book_used():
# #         print("YES")
# #     else:
# #         print("NO")
