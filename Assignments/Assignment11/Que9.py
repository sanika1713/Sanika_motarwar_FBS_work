def squ(li):
    li1 = []
    mul = 1
    for i in range(len(li)):
        mul = li[i] ** 2
        # print(mul)
        li1.append(mul)
    return li1

def cube(li):
    li2 = []
    mul = 1
    for i in range(len(li)):
        mul = li[i] ** 3
        # print(mul)
        li2.append(mul)
    return li2


li = [1,2,3,5,7]
res1 = squ(li)
res2 = cube(li)
print("The original list:",li)
print("square of list:",res1)
print("cube of list:",res2)