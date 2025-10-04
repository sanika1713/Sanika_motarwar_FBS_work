class Book:
    count = 0

    def __init__(self,bid=0,bname="xyz",price=0,author="xyz"):
        Book.count += 1
        self.id = bid
        self.name = bname
        self.p = price
        self.a = author

    def showBook(self):
        print("ID:",self.id)
        print("NAME:",self.name)
        print("PRICE:",self.p)
        print("AUTHOR:",self.a)
        print("############")

    def showcount():
        print("Total Book:",Book.count)

    def __del__(self):
        print('destructor is called')

b1 = Book(101,"How to loose a guy in 10 days",450,"prajakta")
b1.showBook()

print(Book.showcount())