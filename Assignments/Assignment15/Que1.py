class Book:
    def __init__(self,bid=0,bname=" ", price = 0,author =" "):
        self.id = bid
        self.name = bname
        self.p = price
        self.a = author

    def showBook(self):
        print("id:",self.id)
        print("name:",self.name)
        print("price:",self.p)
        print("Author:",self.a)

    def __del__(self):
        print("Destructor is called")

b1 = Book(101,"to good to be true",450,"prajakta kholi")
b1.showBook()

