#LIFO =Last in fast out
books=[ ]
books.append("Learn c")
books.append("Learn c++")
books.append("Learn java")
print(books)
books.pop()
print("Now top book is :",books[-1])
books.pop()
print(books)
books.pop()
print(books)
if not books:
    print("No books left.")
