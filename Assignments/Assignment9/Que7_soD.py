def SOD(n):
    if(n==0):
        return 0
    else:
        return (n%10) + SOD(n//10)

n = int(input("Enter the number:"))
# res = SOD(n)
# print(f'Sum of digit is {res}')
print('sum of digit',SOD(n))