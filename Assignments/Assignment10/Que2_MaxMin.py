li = [23,54,67,87,34,22,1,67]
max = li[0]

for i in range(1,len(li)):
    if(li[i] > max):
        max = li[i]

print("The maximun number is ",max)

min = li[0]
for i in range(1,len(li)):
    if(li[i] < min):
        min = li[i]

print("The minimun element is" , min)