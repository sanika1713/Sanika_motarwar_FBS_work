text = "Hello123World456"

letters = 0
digits = 0

for ch in text:
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        letters += 1
    elif ch >= '0' and ch <= '9':
        digits += 1

print("Number of letters:", letters)
print("Number of digits:", digits)
