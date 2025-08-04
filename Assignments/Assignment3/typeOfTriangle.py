A1 = int(input("Enter the first angle:"))
A2 = int(input("Enter the second angle:"))
A3 = int(input("Enter the third angle:"))
S1 = int(input("Enter the first side:"))
S2 = int(input("Enter the second side:"))
S3 = int(input("Enter the third side"))

if(A1 == A2 == A3):
    print("It is an equilateral triangle.")
elif((A1 == A2 or A2 == A3 or A3 == A1) & (S1 == S2 or S1 == S3 or S1 == S3)):
    print("Triangle is isosceles triangle.")
else:
    print("Triangle is scalene triangle.")