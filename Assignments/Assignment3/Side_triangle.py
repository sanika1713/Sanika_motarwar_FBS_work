s1 = int(input("Enter the first side of the triangle:"))
s2 = int(input("Enter the second side of the triangle:"))
s3 = int(input("Enter the third side of the triangle:"))

if(s1 + s2 > s3 or s2 + s3 > s1 or s1 + s3 > s2):
    print("it is a valid triangle.")
else:
    print("it is not a valid triangle.")