days = int(input("Enter the number of days:"))

years = days // 365

days = days % 365

weeks = days // 7

days = days % 7

print(f'{years}years {weeks}weeks {days}days.')