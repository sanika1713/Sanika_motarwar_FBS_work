def union(li1,li2):
    li3=[]
    for i in range(len(li1)):
        if(li1[i] not in li3):
            li3.append(li1[i])
    

    for j in range(len(li2)):
        if li2[j] not in li3:
            li3.append(li2[j])

    return li3

l1 = [10,20,40]
l2 = [20,30,50]

res = union(l1,l2)
print(res)


