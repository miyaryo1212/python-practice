# 素数計算
print("素数計算")
input_number = int(input("どこまで計算する？数字を入力 (N ≧ 4) >>> "))
for i in range(4, input_number + 1):
    for j in range(2, i + 1):
        if j == i:
            print(i)
            break
        if i % j == 0:
            break