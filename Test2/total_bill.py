p1 = int(input("Enter the price of product1:"))
p2 = int(input("Enter the price of product2:"))
p3 = int(input("Enter the price of product3:"))
p4 = int(input("Enter the price of product4:"))
p5 = int(input("Enter the price of product5:"))

sum = p1 + p2 + p3 + p4 + p5
gst = sum * (18/100)

total_cost = sum + gst 

print(f'The total cost including GST is {total_cost}.')