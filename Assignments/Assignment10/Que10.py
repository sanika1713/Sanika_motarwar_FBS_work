def removeOcc(li , element):
    li1 =[]
    for i in range(len(li)):
        if(li[i] == element):
            pass
        else:
            li1.append(li[i])
    return li1
    
li = [23,54,78,2,78,78,2,2]
ele = int(input("Enter the element:"))

res = removeOcc(li , ele)
print(res)