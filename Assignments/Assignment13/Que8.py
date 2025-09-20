txt = "python is easy language and java is hard language"

w = txt.split()

fre = {}

for word in w:
    if word in fre:
        fre[word] += 1
    else:
        fre[word] = 1

print(fre)