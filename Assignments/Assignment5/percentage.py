num = int(input("Enter total number of students:"))
average = 0

for i in range(1,num+1):
    print(f'marks of student {i}')
    M1=int(input("Enter the marks of subject 1:"))
    M2=int(input("Enter the marks of subject 2:"))
    M3=int(input("Enter the marks of subject 3:"))
    M4=int(input("Enter the marks of subject 4:"))
    M5=int(input("Enter the marks of subject 5:"))

    per = ((M1 + M2 + M3 + M4 + M5)/500)*100
    print(f'Avarage of student {i} is {per}')
    average = average + per

total_average = (average/num)
print(f'Total average of students is {total_average}')




