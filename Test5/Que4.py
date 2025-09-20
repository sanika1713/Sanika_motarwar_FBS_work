li1 = [1,3,4,1,2,3,6,7,1,2,4]


fre = {}

for i in li1:
    if(i in fre):
        fre[i] += 1
    else:
        fre[i] = 1
    
print(fre)

