li = [23,54,6,12,67,45]

max = li[0]
smax = 0

for i in range(1,len(li)):
    if(li[i] > max):
        smax = max
        max = li[i]
    elif(li[i] > smax):
        smax = li[i]

print("Second largest element is" , smax)