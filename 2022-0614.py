# 約数を表示する
from array import array


N = int(input("Nの約数を表示する N >>> "))
array = []
for i in range(1, N + 1):
    if N % i == 0:
        array.append(i)
print(array)