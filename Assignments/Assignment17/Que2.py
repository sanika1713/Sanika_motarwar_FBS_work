class Student:
    def __init__(self,sid=0,nm="NA",age=0,percentage=0):
        self.id = sid
        self.name = nm
        self.a = age
        self.p = percentage

    def display(self):
        print("ID:",self.id)
        print("NAME:",self.name)
        print("PERCENTAGE:",self.p)
        print("RANK:", self.calcRank())
        print("######################")

    def calcRank(self):
        if (self.p >= 75):
            return "Distinction"
        elif(self.p >= 60):
            return "First Class"
        elif(self.p >= 50):
            return "Second Class"
        elif(self.p >= 40):
            return "Pass"
        else:
            return "Fail"
        
    def __str__(self):
        return f"Student \nID={self.id}\nName={self.name}\nAge={self.a}\nPercentage={self.p}\nRank={self.calcRank()}"


class EnggStudent(Student):
    def __init__(self,sid,nm,age,percentage,branch,Internalmarks):
        super().__init__(sid,nm,age,percentage)
        self.b = branch
        self.i = Internalmarks

    def display(self):
        super().display()
        print("BRANCE:",self.b)
        print("INTERNALMARKS:",self.i)
        print("######################")

    def calcRank(self):
        total = (self.i + self.p) / 2
        if total >= 80:
            return "Outstanding"
        elif total >= 70:
            return "Excellent"
        elif total >= 60:
            return "Good"
        elif total >= 50:
            return "Average"
        else:
            return "Needs Improvement"
# s1 = EnggStudent(101,"sandsl",18,99,"cse",67)
# s1.display()

    

id = input("Enter the id:")
name = input("Enter the name:")
age = int(input("Enter the age:"))
per = int(input("Enter the percentage:"))
b = input("Enter the branch:")
IM = int(input("Enter the internal marks:"))

s1 = EnggStudent(id,name,age,per,b,IM)
print(s1)



