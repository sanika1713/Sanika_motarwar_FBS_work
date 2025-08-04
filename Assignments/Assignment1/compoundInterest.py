P = float(input("Enter the value of P:"))
R = float(input("Enter the value of R:"))
T = float(input("Enter the value of T:"))

compoundInterest = P * ((1 + R/100)**T )- P

print(f'compound interest is:{compoundInterest}')