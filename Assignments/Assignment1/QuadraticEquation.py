a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

sqt = ((b**2)-(4*a*c))**0.5

res1 = (-b+sqt)/2*a
res2 = (-b-sqt)/2*a

print(f'the equations of the quadratic erquations are {res1} and {res2}.')