def reverse(n, rev =0):
    if(n == 0):
        return rev
    else:
        d = n % 10
        rev = rev * 10 + d
        return reverse(n // 10, rev)
       
        
n = int(input("Enter the number: "))
res = reverse(n)
print(res)