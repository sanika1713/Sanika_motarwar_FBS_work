def digitCount(num):
    count = 0
    if(num == 0):
        return 0
    else:
        # count = 1 + digitCount(num // 10)
        # print("digitCount",count)
        # return count
        return 1 + digitCount(num // 10)
    
def armstrong(num):
    if(num == 0):
        return 0
    else:
        d = num % 10
        # print("d",d)
        sum = d ** digitCount(temp) + armstrong(num // 10)
        # print("sum",sum)
        return sum
    

    
num = int(input("Enter the number:"))
temp = num
res = armstrong(num)
# print(res)

if(num == res):
    print("The number is Armstrong.")
else:
    print("The number is not Armstrong.")