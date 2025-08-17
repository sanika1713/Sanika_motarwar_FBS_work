userId = "sanikamotarwar@1713"
password = "SANIKA17"
count = 0

while(count < 3):
    id =input("Enter the user ID:")
    num =input("Enter the password:")
    count = count
if(userId == id and password == num):
    print("Valid user")
else:
    if(count < 3):
        print("wrong credentials")
    else:
        print("Try again later")