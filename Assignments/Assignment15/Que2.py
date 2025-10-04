class product:
    def __init__(self,pid=0,pname=" ",price=0,quantity=0):
        self.id = pid
        self.name = pname
        self.p = price
        self.q = quantity

    def ShowProduct(self):
        print('product id:' , self.id)
        print('product name:',self.name)
        print('Product price:',self.p)
        print('quantity:',self.q)

    def __del__(self):
        print('Destructor is called')

p1 = product(101,"phone",4500,1)
p1.ShowProduct()
        