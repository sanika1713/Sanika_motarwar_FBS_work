text = "this is assignment number eleven"
cWords = 1
Length = 0

for ch in text:
    if(ch == ' '):
        cWords += 1
print(f'Total numbers of words:{cWords} ')

for ch in text:
    Length += 1
print(f'number of characters in the string:{Length}')