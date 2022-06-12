# 素数計算
print("素数計算")
input_number = int(input("どこまで計算する？数字を入力 (N ≧ 5) >>> "))
totarl_calc = 0
for i in range(4, input_number + 1):
    for j in range(2, i + 1):
        totarl_calc += 1
        if j == i:
            print(i)
            break
        if i % j == 0:
            break
print("==============================")
print(f'{"合計試行回数："}{str(totarl_calc)}')
print("==============================")