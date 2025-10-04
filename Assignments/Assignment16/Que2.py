class Product:

    def __init__(self,pname="xyz",price=0,quantity=0):
        self.name = pname
        self.p = price
        self.q = quantity

    def showProduct(self):
        print("NAME:",self.name)
        print("PRICE:",self.p)
        print("QUANTITY:",self.q)

    @staticmethod
    def discount(price):
        totalPrice = price - price * 0.2
        print("Total price after discount is:",totalPrice)

    def __del__(self):
        print('destructor is called')

p1 = Product("fkvm",1000,3)
p1.showProduct()
p1.discount(p1.p)


