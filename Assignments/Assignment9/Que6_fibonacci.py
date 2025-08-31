def fibo(num , n1=-1 , n2 =1):
    if (num == 0):
        return 
    else:
        n3 = n1 + n2
        print(n3, end =" ")
        fibo(num -1 ,n2 , n3)


num =int(input("Enter the number:"))
fibo(num)