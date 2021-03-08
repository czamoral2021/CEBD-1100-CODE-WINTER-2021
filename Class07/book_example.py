class Book:
    title = ""
    ISBN = ""

book1 = Book()
book1.title = "War of the Worlds"
book1.ISBN = "123456789"

book2 = Book()
book2.title = "Insomnia"
book2.ISBN = "234567890"

book3 = Book()
book3.title = "Insomnia"
book3.ISBN = None

array_of_books = [book1, book2]

for b in array_of_books:
    print(b.title)



