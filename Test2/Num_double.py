num = int(input("Enter three digit number:"))
temp = num

n1 = temp % 10 
temp = temp // 10

n2 = temp % 10
temp = temp // 10

n3 = temp % 10 

# print(f'{n1}{n2}{n3}')
if( n2 * 2 == n3   and n1 * 0.5 == n3 ):
    print("yes, you have done it. ")
else:
    print("please try next time.")