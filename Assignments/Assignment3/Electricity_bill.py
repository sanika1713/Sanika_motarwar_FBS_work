E_unit = int(input("Enter the electricity unit:"))
total_bill = 0

if(E_unit > 0):
    if(E_unit > 50):
        if(E_unit > 150):
            if(E_unit > 250):
                total_bill = 50 * 0.5 + 100 * 0.75 + 100 * 1.20
                unit4 = E_unit - 250
                total_bill = total_bill + unit4 * 1.50
            else:
                total_bill = 50 * 0.5 + 100 * 0.75
                unit3 = E_unit - 150
                total_bill = total_bill + unit3 * 1.20
        else:
            total_bill = 50 * 0.5
            unit2 = E_unit - 50
            total_bill = total_bill + (unit2 * 0.75)
    else:
        total_bill = E_unit * 0.5
        print(f'')
else:
    print("Invalid input")

print(total_bill)

# total_bill = total_bill + total_bill * 0.2
# print(f'Total Bill is {total_bill}')

###