def sum(num):
    total = 0
    for i in range(1,num+1):
        total += i
    print(total)

n = int(input("Enter the number:"))
sum(n)
