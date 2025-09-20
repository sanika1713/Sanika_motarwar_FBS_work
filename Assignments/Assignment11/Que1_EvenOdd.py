def EvenOdd(li):
    li1=[]
    li2=[]
    
    for i in range(len(li)):
        if(li[i] %2 == 0):
            li1.append(li[i])
        else:
            li2.append(li[i])
    return (li1,li2)

li = [1,2,3,4,5,6,7,8,9]
li,li2 = EvenOdd(li)
print(f'Even:',li)
print(f'odd:',li2)