num = int(input("Enter the number to check:"))
temp = num
count = 0
mul = 1
sum = 0

while(temp>0):
    d = temp % 10 
    count = count + 1
    temp = temp // 10
# print(count)


temp = num
while(temp > 0):
    d = temp % 10
    temp = temp // 10
    mul = d ** count
    sum = sum + mul

if(num == sum):
    print("Amstrong number.")
else:
    print("Not a amstrong number.")
