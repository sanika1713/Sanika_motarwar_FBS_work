D = [2000,500,200,100,50,20,10,5]

amt = int(input("Enter the amount:"))
count = 0
for ele in D:
    while (amt >= ele):
        # print(ele)
        amt = amt - ele
        count += 1

print("Minimum number of notes:",count)
    