for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=" ")

    for j in range(1,1+i):
        print(chr(64+j),end=" ")

    for j in range(i + 1,2 *i):
        print(chr(64+j),end=" ")
    
    print()

#         A 
#       A B C
#     A B C D E
#   A B C D E F G
# A B C D E F G H I