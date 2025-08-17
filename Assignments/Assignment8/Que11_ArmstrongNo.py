def count_digit(n):
        no = 0
        temp = n
        while(temp>0):
            
            no = no + 1
            temp = temp // 10
        return no


def Arm(n):
    digit = count_digit(n)
    temp = n
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        sum += d ** digit
    return sum
        

N1 = int(input("Enter the number to check:"))
if(N1 == Arm(N1)):
            print("Amstrong number.")
else:
    print("Not a amstrong number.")