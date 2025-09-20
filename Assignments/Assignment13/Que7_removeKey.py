d1 = {'a':10,'b':30,'c':40}

k = input("Enter the key to pop:")

if k in d1:
    d1.pop(k)
    print(d1)
else:
    print('key not found.')