t1 = "this is assignment number eleven"
t2 = "Firstbit solutions"

c1 = 0 
c2 = 0

for ch in t1:
    c1 += 1

for ch in t2:
    c2 += 1

if(c1>c2):
    print(t1)
else:
    print(t2)