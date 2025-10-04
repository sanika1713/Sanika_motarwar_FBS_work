class shirt:
    def __init__(self,sid =0,sname=" ",type=" ",price = 0,size="m"):
        self.id = sid
        self.name = sname
        self.t = type
        self.p = price
        self.s = size

    def showShirt(self):
        print('id:',self.id)
        print('name:',self.name)
        print('type:',self.t)
        print('price:',self.p)
        print('size:',self.s)

    def __del__(self):
        print('destructor is called')

s1 = shirt(111,'xyz','formal',5000,'small')
s1.showShirt()
