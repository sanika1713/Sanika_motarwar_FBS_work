cost_price = int(input("Enter the base price:"))
discount = int(input("Enter the discount:"))

dis = cost_price * (discount/100)
selling_price = cost_price + dis

print(f'Selling price is {selling_price}')