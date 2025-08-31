def pat(num):
    for i in range(1,num+1):
        for j in range(1,num+1):
            if(i==1 or i==num or i+j==num+1):
                  print('*',end=" ")
            else:
                 print(' ',end=" ")

        print()


n = int(input("Enter the number:"))
print(pat(n))

