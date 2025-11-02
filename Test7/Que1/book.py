class Book():
    def __init__(self,bid= None,name = None,price=None,author= None):
        self.bid = bid
        self.nm = name
        self.p = price
        self.a = author

    def __str__(self):
        return f'{self.bid}, {self.nm}, {self.p}, {self.a}'
    
    def Addbook():
        pass
    def Delbook():
        pass
    def showall():
        pass
    def search():
        pass

    




if(__name__ == '__main__'):
    b1 = Book(101,'Too good to be true',450,'prajikta kholi')
    print(b1)