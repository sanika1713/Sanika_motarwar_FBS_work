text = "Firstbit solution"
newStr = ' '

for i in range(len(text)):
    if(i %2 == 0):
        newStr += text[i]
    else:
        continue

print(newStr)