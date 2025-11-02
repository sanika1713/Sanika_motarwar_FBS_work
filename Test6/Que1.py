class vehical():
    def __init__(self,person):
        self.p = person

class wheeler2(vehical):
    def total_toll(self):
        base_toll = 20
        if(self.p <= 2):
            return base_toll
        else:
            return base_toll + (self.p - 2) * 10
        
class wheeler3(vehical):
    def total_toll(self):
        base_toll = 30
        if(self.p <= 3):
            return base_toll
        else:
            return base_toll + (self.p - 3) * 20
        
class wheeler4(vehical):
    def total_toll(self):
        base_toll = 40
        if(self.p <= 4):
            return base_toll
        else:
            return base_toll + (self.p - 4) * 40
        
class heavyVehical(vehical):
    def total_toll(self):
        base_toll = 60
        if(self.p <= 6):
            return base_toll
        else:
            return base_toll + (self.p - 6) * 100

        
  

ch = 0
while(ch != '5'):
    print('''Please select option from bellow:
          1. 2 wheeler
          2. 3 wheeller
          3. 4 wheeler
          4. Heavy vehical
          5. Exit''')
    ch = input("Enter your choice:")
    person = int(input("Enter number of person:"))

    if(ch == '1'):
        v = wheeler2(person)

    elif(ch == '2'):
        v =wheeler3(person)
        
    elif(ch == '3'):
        v = wheeler4(person)

    elif(ch == '4'):
        v = heavyVehical(person)

    else:
        break

    print(f'Total Toll to pay:{v.total_toll()}')


