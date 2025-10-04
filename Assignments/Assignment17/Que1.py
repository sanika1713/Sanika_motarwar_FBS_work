class Student:
    def __init__(self,id=0,nm="NA",age=0,percentage=0):
        self.StudentID = id
        self.name = nm
        self.age =age
        self.p = percentage

    def displaData(self):
        print("StudentID:",self.StudentID)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Percentage:",self.p)
        print("Rank:",self.calcRank())

# s1 = Student(10,'virat',18,90)
# s1.displaData()

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
        return f"Student \nID={self.StudentID}\nName={self.name}\nAge={self.age}\nPercentage={self.p}\nRank={self.calcRank()}"

ID = int(input("Enter the id:"))
name = input("Enter the name:")
age = int(input("Enter the age:"))
per = int(input("Enter the percentage:"))

S1 = Student(ID,name,age,per)
# S1.displaData()
print(S1)

