# 素数計算
import time

primenumber_logo = "■"
NOT_primenumber_logo = "□"

print("素数の分布")

input_number = int(input("どこまで計算する？数字を入力 (N ≧ 2) >>> "))

t0 = time.time()

total_calc = 0
output_list = []

for i in range(1, input_number + 1):
    if i == 1:
        output_list.append(NOT_primenumber_logo)
    else:
        for j in range(2, i + 1):
            total_calc += 1
            if j == i:
                output_list.append(primenumber_logo)
                break
            if i % j == 0:
                output_list.append(NOT_primenumber_logo)
                break

t1 = time.time()
total_time = t1 - t0

output_list_format = "".join(output_list)
print(output_list_format)

print("==============================")
print(f'{"合計計算回数："}{str(total_calc)}')
print(f'{"経過時間 (計算)："}{str(total_time)}')
print(f'{"calc / time = "}{total_calc / total_time}')
print("==============================")