num = int(input("Enter three digit number:"))
temp = num

d1 = temp % 10
temp = temp //10

d2 = temp % 10
temp = temp //10

d3 = temp % 10
temp = temp //10

print(f'D1:{d1}, D2:{d2}, D3:{d3}')

