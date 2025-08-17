def leapYear(year):
    if(year % 4 == 0):
        print(f'{year} is a leap year.')
    else:
        print(f'{year} is not a leap year.')

n = int(input("Enter the year:"))
leapYear(n)