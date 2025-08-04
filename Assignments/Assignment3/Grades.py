M1 = int(input("Enter Marks 1:"))
M2 = int(input("Enter Marks 2:"))
M3 = int(input("Enter Marks 3:"))
M4 = int(input("Enter Marks 4:"))
M5 = int(input("Enter Marks 5:"))

sum = M1 + M2 + M3 + M4 + M5

if(sum >= 45):
    print("First class")
elif(sum >= 40):
    print("Second class")
elif(sum >= 35):
    print("Third class")
elif(sum >= 30):
    print("Fourth class")
elif(sum >= 25):
    print("Fifth class")
else:
    print("Fail")