
def reverse(num, rev = 0):
    
    if(num == 0):
        return rev
    else:
        return reverse(num // 10, rev * 10 + num % 10)
    
def palindrome(num):
    if(num == reverse(num)):
        print("The number is pallindrome.")
    else:
        print("The number is not pallindrome.")

num =int(input("Enter the number:"))
palindrome(num)
