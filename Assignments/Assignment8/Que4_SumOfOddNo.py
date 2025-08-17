def sum(num):
    sum = 0
    for i in range(1,num+1):
        if(i%2 == 0):
            pass
        else:
            sum = sum + i

    print(f'the sum is {sum}')

n = int(input("Enter the number:"))
sum(n)