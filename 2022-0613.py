# 素数計算
import time

print("素数計算")

input_number = int(input("どこまで計算する？数字を入力 (N ≧ 2) >>> "))

t0 = time.time()

total_calc = 0
for i in range(2, input_number + 1,):
    for j in range(1, i + 1, 2):
        if j != 1:
            total_calc += 1
            if j == i:
                print(i)
                break
            if i % j == 0:
                break

t1 = time.time()
total_time = t1 - t0

print("==============================")
print(f'{"合計計算回数："}{str(total_calc)}')
print(f'{"経過時間 (計算)："}{str(total_time)}')
print(f'{"calc / time = "}{total_calc / total_time}')
print("==============================")