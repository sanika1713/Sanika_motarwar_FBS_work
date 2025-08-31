def SOS(n):
    if(n == 0):
        return 0
    else:
        return n + SOS(n-1)
    
n = int(input("Enter the number:"))
sum = SOS(n)
print(sum)