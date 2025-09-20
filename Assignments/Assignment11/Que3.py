

data = [[1, 9,4], [3, 5,3], [4, 1,2], [2, 7,9], [6, 3,11]]

n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        if data[j][1] > data[j + 1][1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print("Sorted list:", data)
