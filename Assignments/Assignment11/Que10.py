def removeEven(li):
    l1=[]
    for i in range(len(li)):
        if(li[i] %2 == 0):
            pass
        else:
            l1.append(li[i])
    return l1

li = [1,2,3,4,5,6,7,8,9]
res = removeEven(li)
print(res)