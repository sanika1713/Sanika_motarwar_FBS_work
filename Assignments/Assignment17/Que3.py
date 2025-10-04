from Student import Student

class MedicalStudent(Student):
    def __init__(self,id=0,nm="NA",age=0,percentage=0,spec="xyz",Marks=0):
        super().__init__(id,nm,age,percentage)
        self.s = spec
        self.m = Marks

    def showdata(self):
        # super().displaydata()
        # print("Specialization:",self.s)
        # print("Marks of intership:",self.m)

        return super().displayData() + f'\nSpecialization:{self.s}\nMarks of intership:{self.m}'


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
        return f'ID:{self.StudentID}\nNAME:{self.name}\nAGE:{self.age}\nPERCENTAGE:{self.p}\nSPEC:{self.s}\nMARKS:{self.calcRank()}'
    

    def calcRank(self):
        total = (self.m + self.p) / 2
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

# m1 = MedicalStudent(101,"virat",18,89,"xyz",10)
# print(m1.showdata())

id = int(input("Enter the id:"))
name = input("Enter the name:")
age = int(input("Enter the age:"))
per = int(input("Enter the percentage:"))
sp = input("Enter the specialization:")
m = int(input("Enter the marks of intership:"))

m1 = MedicalStudent(id,name,age,per,sp,m)
# print(m1.showdata())
print(m1)
