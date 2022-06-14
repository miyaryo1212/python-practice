num = 0
for i in range(1, 100001):
    array = []
    for j in range(1, i + 1):
        if i % j == 0:
            array.append(j)
    if len(array) >= num:
        num = len(array)

print(num)