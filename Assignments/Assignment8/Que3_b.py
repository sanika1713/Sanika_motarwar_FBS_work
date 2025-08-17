
def fact(num):
    total = 0
    mul = 1
    for i  in range(1,num+1):
        mul *=i
        total += mul

    print(f'The total is {total}')


n = int(input("Enter the number:"))
fact(n)