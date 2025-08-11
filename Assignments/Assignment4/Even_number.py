# n = int(input("Enter the value of n:"))
# i = 1

# while(i <= n):
#     if(i % 2 ==0 ):
#         print(i)
#     else:
#         pass
#     i = i + 1


n = int(input("Enter the value of n:"))

for num in range(1,n+1):
    if(num % 2 == 0):
        print(num, end=" "  )
    else:
        pass
    