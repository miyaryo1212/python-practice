from ctypes.wintypes import PINT
from itertools import count


n = int(input("入力 >>> "))
output_text = ""
for i in range(2, n + 1):
    for j in range (2, i + 1):
        if j == i:
            output_text += f'{str(i)}{" ,"}'
        if i % j == 0:
            break
num = output_text.count("1")
print(num)