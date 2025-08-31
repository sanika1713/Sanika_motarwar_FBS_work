def div(li ,m, n):
    li1 =[]
    for i in range(len(li)):
        if(li[i] % m == 0 and li[i] % n == 0):
            li1.append(li[i])
    return li1
    
li = [2,4,6,8,10,12,3,45,23,4]
m = int(input("Enter the first number:"))
n = int(input("Enter the second number:"))


res = div(li,m,n)
print(res)