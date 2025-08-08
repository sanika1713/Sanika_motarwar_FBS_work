l = int(input("Enter the length of the wall:"))
cost = int(input("Enter the cost of painting:"))

area = l * l
Total_area = 4 * area
total_cost = Total_area * cost

print(f'The total cost to paint the interior is {total_cost}.')