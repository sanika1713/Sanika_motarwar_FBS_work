def power(m, n):
    if m == 0 and n == 0:
        return "undefined"
    if n == 0:
        return 1
    if n > 0:
        return m * power(m, n - 1)
    else:
        return 1 / power(m, -n)

    
m = int(input("Enter the number:"))
n = int(input("Enter the number:"))
res = power(m,n)
print(res)