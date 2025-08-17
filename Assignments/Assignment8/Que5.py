def AddPrime(Num):
    count = 0
    num = 2
    sum = 0

    while(count < n):
        for i in range(2,(num//2)+1):
            if(num%i == 0):
                break
        else:
            count = count + 1
            sum = sum + num
        num = num + 1


    print(f'The sum is {sum}')

n = int(input("Enter the number:"))
AddPrime(n)