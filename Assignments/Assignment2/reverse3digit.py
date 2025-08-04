num = int(input("Enter a three digit number:"))
temp = num

n1 = temp % 10
temp = temp // 10

n2 = temp % 10
temp = temp // 10

n3 = temp % 10
temp = temp // 10

print(f'the reverse of the number{temp} is {n1}{n2}{n3}')
