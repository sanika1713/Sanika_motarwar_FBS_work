def union(li1,li2):
    li3=[]
    for i in range(len(li1)):
        if(li1[i] in li2):
            li3.append(li1[i])
    return li3

l1 = [1,2,34,4,55,63,45]
l2 = [2,11,34,45,7]

res = union(l1,l2)
print(res)