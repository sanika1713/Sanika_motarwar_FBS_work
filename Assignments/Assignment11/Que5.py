words = ["apple", "bat", "banana", "cats", "a"]

n = len(words)

for i in range(n):

    min_index = i
    for j in range(i + 1, n):
        if len(words[j]) < len(words[min_index]):
            min_index = j
    
    words[i], words[min_index] = words[min_index], words[i]

print("Sorted list by length:", words)
