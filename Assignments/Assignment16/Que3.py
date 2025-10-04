class shirt:
    def __init__(self,sid=0,sname="xyz",type="NA",price=0,size="NA"):
        self.id = sid
        self.name = sname
        self.t = type
        self.p = price
        self.s = size

    def showShirt(self):
        print("ID:",self.id)
        print("Name:",self.name)
        print("TYPE:",self.t)
        print("PRICE:",self.p)
        print("SIZE:",self.s)

    def finalPrize(self):
        if(self.s == "small"):
            p = self.p + self.p * 0.1
            print("Final Price:",p)
        elif(self.s == "medium"):
            p = self.p + self.p * 0.2
            print("Final Price:",p)
        elif(self.s == "large"):
            p = self.p + self.p * 0.3
            print("Final Price:",p)
        else:
            print("Enter valid shirt size")



    def __del__(self):
        print('destructor is called')

s1 = shirt(10,"ddsd","formal",1000,"large")
s1.showShirt()
s1.finalPrize()