TotalMoney = int(input("Enter the total amount:"))
temp = TotalMoney

Note2000 = temp // 2000
temp = temp % 2000

Note500 = temp // 500
temp = temp % 500

Note200 = temp // 200
temp = temp %  200

Note100 = temp // 100
temp = temp %  100

Note50 = temp // 50
temp = temp % 50

Note20 = temp // 20
temp = temp % 20

Note10 = temp // 10
temp = temp % 10



print(f'Minimun number of notes for:{TotalMoney} are 2000:{Note2000} , 500:{Note500}, 200:{Note200}, 100:{Note100}, 50:{Note50}, 20:{Note20}, 10:{Note10}.')
minNote= Note2000 + Note500 + Note100 + Note200+ Note50 + Note20 + Note10 
print(f'total notes:{minNote} ')