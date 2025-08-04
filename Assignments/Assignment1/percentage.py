M1 = int(input("Enter the marks of subject 1:"))
M2 = int(input("Enter the marks of subject 2:"))
M3 = int(input("Enter the marks of subject 3:"))
M4 = int(input("Enter the marks of subject 4:"))
M5 = int(input("Enter the marks of subject 5:"))

total_marks = M1+M2+M3+M4+M5
percentage = (total_marks/500) * 100

print(f'average of marks is {percentage}%.')