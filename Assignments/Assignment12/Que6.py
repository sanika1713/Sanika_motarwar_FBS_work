text = "this is assignment number eleven"
newStr = ''

for ch in text:
    if(ch == ' '):
        newStr += '!'
    else:
        newStr += ch
print(newStr)