def fac(n):
    if(n == 1):
         return 1    
    else:
        return n * fac(n-1)
    
def sum(n):
    if(n == 1):
        return 1
    else:
        return fac(n)+sum(n-1)
    

n = int(input("Enter nuumber:"))
res = sum(n)
print(res)
 
