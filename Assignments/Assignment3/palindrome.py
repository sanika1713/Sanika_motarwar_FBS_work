num1 = int(input("Enter a three digit number:"))
temp = num1 

d1 = temp % 10
temp = temp // 10 

d2 = temp % 10
temp = temp // 10

d3 = temp % 10

# print(f'{d3} {d2} {d1}')

rev = (d1*100)+(d2*10)+d3

if(num1 == rev):
    print(f'The number {num1} is a palindrome.')
else:
    print("It is not a palindrome.")
