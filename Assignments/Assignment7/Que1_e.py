for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end=" ")
    for j in range(1,6):
        if(j==1 or i==j or i==5):
            print(j,end="   ")
        else:
            print("  ",end="  ")
    print()

#         1
#       1   2
#     1       3
#   1           4
# 1   2   3   4   5