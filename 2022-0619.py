# 素数計算
import time

print("素数計算")

input_number = int(input("素数判定 (N ≧ 2) >>> "))

t0 = time.time()

total_calc = 0
for i in range (2, input_number + 1):
    total_calc += 1
    if i == input_number:
        print(f'{str(input_number)}{"は素数"}')
        break

    if input_number % i == 0:
        print(f'{str(input_number)}{"は"}{str(i)}{"で割れる"}')
        break

t1 = time.time()
total_time = t1 - t0

print("==============================")
print(f'{"合計計算回数："}{str(total_calc)}')
print(f'{"経過時間 (計算)："}{str(total_time)}')
print(f'{"calc / time = "}{total_calc / total_time}')
print("==============================")