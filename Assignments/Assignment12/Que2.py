text = 'firstbit solutions'
newStr = ''
ind = int(input("Enter the index:"))

for i in range(len(text)):
    if i == ind:
        continue
    else:
        newStr += text[i]

print(newStr)