A1 = int(input("Enter the age of first member:"))
A2 = int(input("Enter the age of second member:"))
A3 = int(input("Enter the age of third member:"))
A4 = int(input("Enter the age of fourth member:"))
A5 = int(input("Enter the age of fifth member:"))

ticket_amt = int(input("Enter the cost of ticket:"))

##For person 1
if(A1 < 12 ):
    dis_amt = ticket_amt * 0.3
    amt1 = ticket_amt - dis_amt
elif(A1 > 59):
    dis_amt = ticket_amt * 0.5
    amt1 = ticket_amt - dis_amt
else:
    amt1 = ticket_amt

##person 2
if(A2 < 12 ):
    dis_amt = ticket_amt * 0.3
    amt2 = ticket_amt - dis_amt
elif(A2 > 59):
    dis_amt = ticket_amt * 0.5
    amt2 = ticket_amt - dis_amt
else:
    amt2 = ticket_amt

##person 3
if(A3 < 12 ):
    dis_amt = ticket_amt * 0.3
    amt3 = ticket_amt - dis_amt
elif(A3 > 59):
    dis_amt = ticket_amt * 0.5
    amt3 = ticket_amt - dis_amt
else:
    amt3 = ticket_amt

##person 4
if(A4 < 12 ):
    dis_amt = ticket_amt * 0.3
    amt4 = ticket_amt - dis_amt
elif(A4 > 59):
    dis_amt = ticket_amt * 0.5
    amt4 = ticket_amt - dis_amt
else:
    amt4 = ticket_amt


##person 5
if(A5 < 12 ):
    dis_amt = ticket_amt * 0.3
    amt5 = ticket_amt - dis_amt
elif(A5 > 59):
    dis_amt = ticket_amt * 0.5
    amt5 = ticket_amt - dis_amt
else:
    amt5 = ticket_amt

Total_amount = amt1 + amt2 + amt3 + amt4 + amt5

print(f'Total amount is {Total_amount}')
