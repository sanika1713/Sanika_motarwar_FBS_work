d1 = {1:'python',2:'java'}
d2 = {3:'c',4:'c++'}

# d1.update(d2)
# print(d1)

for key in d2:
    d1[key] = d2[key]
print(d1)