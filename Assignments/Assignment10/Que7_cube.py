def cube(li):
    li1 = []
    mul = 1
    for i in range(len(li)):
        mul = li[i] ** 3
        # print(mul)
        li1.append(mul)
    return li1


li = [2,3,4,5,6]
res = cube(li)
print(res)

