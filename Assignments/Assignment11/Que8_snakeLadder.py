bord = []
for i in range(9, -1 , -1):
    row = []
    for j in range((i* 10) + 1 , (i * 10)+11):
        # print(j, end =" ")
        row.append(j)
    if(i % 2 != 0):
        row.reverse()
    bord.append(row)

print(bord)
