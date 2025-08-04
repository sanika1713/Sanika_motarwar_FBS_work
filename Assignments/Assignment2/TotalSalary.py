BaseSalary = int(input("Enter the base salary:"))

da = BaseSalary * (10/100)
ta = BaseSalary * (12/100)
hra = BaseSalary * (15/100)

FinalSalary = BaseSalary + da + ta + hra

print(f'The total salary is:{FinalSalary}')