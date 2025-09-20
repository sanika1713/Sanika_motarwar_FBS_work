d1 = {1: 'python', 2: 'java', 3: 'c', 4: 'c++'}

k =int(input("Enter the value:"))

for key in d1:
    if(k==key):
        print(f'{k} is present in dictonary.')
        break
else:
    print('key is not present.')