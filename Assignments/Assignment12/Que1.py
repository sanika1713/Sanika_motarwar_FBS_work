# str = " sanika"
# print(str.replace('a','@'))

str = 'Firstbit solution'
newstr = ''
for ch in str:
    if ch == 'i':
        newstr += '$'
    else:
        newstr += ch
print(newstr)


