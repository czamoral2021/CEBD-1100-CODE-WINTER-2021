class Book:
    title = ""
    ISBN = ""

book1 = Book()
book1.title = "War of the Worlds"
book1.ISBN = "123456789"

book2 = Book()
book2.title = "Insomnia"
book2.ISBN = "23456789"

# print(book2.title)
array_of_books = [book1, book2]

for b in array_of_books:
    print(b.title)



