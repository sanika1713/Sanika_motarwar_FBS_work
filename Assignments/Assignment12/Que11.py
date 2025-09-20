text = "this Question is repeated"
newStr = ''

for ch in text:
    if(ch == ' '):
        newStr += '!'
    else:
        newStr += ch
print(newStr)