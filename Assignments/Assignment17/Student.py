class Student:
    def __init__(self,id=0,nm="NA",age=0,percentage=0):
        self.StudentID = id
        self.name = nm
        self.age =age
        self.p = percentage

    def displayData(self):
        # print("StudentID:",self.StudentID)
        # print("Name:",self.name)
        # print("Age:",self.age)
        # print("Percentage:",self.p)

        return f'Student ID:{self.StudentID}\nName:{self.name}\nAge:{self.age}\nPercentage:{self.p}'

# s1 = Student(10,'virat',18,90)
# s1.displaData()

