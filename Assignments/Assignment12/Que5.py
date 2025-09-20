text = 'firstbit solutions'
S = text.lower()
count = 0
for ch in S:
    if(ch == 'a' or ch =='e' or ch == 'i'or ch =='o' or ch == 'u'):
        count += 1

print(f'Total no of vowels:{count}')