def evenOdd(li):
    li2 = []
    li3 = []
    for i in range(len(li)):
        if(li[i] %2 ==0):
            li2.append(li[i])
        else:
            li3.append(li[i])
    return li2,li3

li = [2,4,6,5,11,55,76,89]
even,odd = evenOdd(li)
print("Even Number:" , even)
print("odd number:",odd)
