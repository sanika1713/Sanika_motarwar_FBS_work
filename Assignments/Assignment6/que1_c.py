for i in range(0,4):
    for j in range(0,4-i):
        print(' ',end="")
    num = 1
    for j in range(0,1+i):
        print(num,end=" ")
        num = num *(i-j)//(j+1)
    print()

#     1 
#    1 1
#   1 2 1
#  1 3 3 1