emp = int(input("Enter the number of employes:"))
Total_salary = 0

for i in range(1,emp+1):
    base_salary = int(input("Enter the base salary of employee:"))

    if(base_salary>20000):
        da = base_salary * 0.1
        ta = base_salary * 0.12
        hra = base_salary * 0.15
        total_salary = base_salary + da + ta + hra
        print(f'Total salary of employ {i} is {total_salary}')
        Total_salary = Total_salary + total_salary

    else:
        da = base_salary * 0.15
        ta = base_salary * 0.18
        hra = base_salary * 0.2
        total_salary = base_salary + da + ta + hra
        print(f'Total salary of employ {i} is {total_salary}')
        Total_salary = Total_salary + total_salary

print(f'The total salary of {i} employees is {Total_salary}.')
       