total_passenger =int(input("Enter total number of passengers:"))
Base_price =int(input("Enter the base price of the ticket:"))
total_price = 0

for i in range(1,total_passenger+1):
    age =int(input("Enter the age of the passenger:"))
    if(age < 12):
        price = Base_price - (Base_price * 0.3)
        total_price = total_price + price
    elif(age > 59):
        price = Base_price - (Base_price * 0.5)
        total_price = total_price + price
    else:
        total_price = total_price + price

print(total_price)

