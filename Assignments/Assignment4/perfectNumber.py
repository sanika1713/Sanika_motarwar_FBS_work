num =int(input("Enter the number:"))
sum = 0
for i in range(1,num):
    if(num%i == 0):
        sum = sum + i
    else:
        pass
if(sum == num):
        print("perfect number.")
else:
    print("not perfect number.")    