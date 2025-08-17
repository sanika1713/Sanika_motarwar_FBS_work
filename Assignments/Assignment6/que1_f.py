
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=" ")

    for j in range(1,1+i):
        print(j,end=" ")

    for j in range(i + 1,2 *i):
        print(j,end=" ")
    
    print()


#         1 
#       1 2 3
#     1 2 3 4 5
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9