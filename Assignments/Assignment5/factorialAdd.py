
num = int(input("Enter the number: "))
total = 0
fact = 1
i = 1
while i <= num:
    fact *= i
    total += fact
    i += 1

print(total)
