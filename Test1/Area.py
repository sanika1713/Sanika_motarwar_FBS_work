l = int(input("Enter the lenght:"))
b = int(input("Enter the breadth:"))
r = int(input("Enter the radius:"))

###Area

Area_rec = l * b
Area_Circle = 0.5 * 3.14 * r * r

Total_area = Area_rec + Area_Circle

print(f'Total area of the figure is:{Total_area}')

###perimeter

perimeter_rectangle = 2 * l + b
cerference_of_circle = 3.14 * r

Total_perimeter = perimeter_rectangle + cerference_of_circle

print(f'Total perimeter of the figure is {Total_perimeter}')