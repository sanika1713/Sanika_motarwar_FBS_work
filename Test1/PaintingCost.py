###Assuming that length and breadth of the wall are same
l = int(input("Enter the lenght of the wall:"))
cost = int(input("Enter the cost of painting the wall:"))

Area_of_1_wall = l * l
Area_of_6_walls = 6 * Area_of_1_wall

Area_of_Remaining_wall = ((l/2) * (l/2)) * 3

Total_area = Area_of_6_walls + Area_of_Remaining_wall

Total_cost = Total_area * cost * 2


print(f'Toatal area of the wall is:{Total_area} and cost to paint is {Total_cost}.')

