num = int(input("Enter the number:"))
temp = num
sum = 0

while(temp > 0):
    d = temp % 10
    temp = temp // 10

    fact = 1
    i = 1

    while(i <= d):
        fact = fact * i
        i = i + 1

    sum = sum + fact

if(sum == num):
    print("It is a strong number.")
else:
    print("Not a strong number.")