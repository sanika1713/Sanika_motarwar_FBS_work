def duplicate(li):
    li1 = []
    for i in range(len(li)):
        if(li[i] not in li1):
            li1.append(li[i])
    return li1

li = [12,34,2,13,12,6,76,56,6]
res = duplicate(li)
print(res)