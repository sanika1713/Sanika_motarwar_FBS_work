def fib(num):
    n1 = 1
    n2 = 0
    i = 1
    while(i<=num):
        sum = n1 + n2
        print(sum)
        n1 = n2
        n2 = sum
        i = i+1


num = int(input("Enter the number:"))
fib(num)

