# 素数判定
print("素数判定")
input_number = int(input("数字を入力 >>> "))
for i in range (2, input_number + 1):
    if i == input_number:
        print(f'{str(input_number)}{"は素数"}')
        break

    if input_number % i == 0:
        print(f'{str(input_number)}{"は"}{str(i)}{"で割れる"}')
        break