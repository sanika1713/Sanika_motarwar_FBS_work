###swapping of number using third variable

x = 10 
y = 20


temp = x
x = y
y =temp

print(f'After swapping x:{x}, y:{y}')


###without using third variable###

x = 17
y = 9

x = x + y

y = x - y

x = x - y

print(f'After swapping x:{x}, y:{y}')


x = 33
y = 44

x , y = y , x
print(f'After swapping x:{x}, y:{y}')