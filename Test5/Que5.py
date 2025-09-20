def union(li1,li2):
    li3=[]
    for i in li1:
        if(i not in li2):
            li3.append(i)
    for i in li2:
        if(i not in li3):
            li3.append(i)
    return li3

l1 = [10,20,40,60]
l2 = [20,30,60,90]

res = union(l1,l2)
print(res)