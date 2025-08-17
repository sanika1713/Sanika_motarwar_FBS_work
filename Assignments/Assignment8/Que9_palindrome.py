def palindrome(n):
    temp = n
    rev = 0
    while(temp > 0 ):
        d = temp % 10
        rev = rev * 10 + d
        temp = temp // 10
    # print(rev)
    
    if(n == rev):
        print("The number is palindrome.")
    else:
        print("Not a palindrome")

num = int(input("Enter a number:"))
palindrome(num)