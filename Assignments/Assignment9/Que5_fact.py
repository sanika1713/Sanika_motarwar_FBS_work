def fac(n):
    if(n ==0):
        return 1
    else:
        return n * fac(n-1)
    
n = int(input("Enter the number:"))
factorial = fac(n)
print(factorial)