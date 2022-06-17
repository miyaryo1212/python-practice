import random
input_num = int(input("乱数を生成して降順に表示 >>> "))
output_list = []
for i in range(input_num + 1):
    random_num = random.randrange(1, 1000)
    output_list.append(random_num)

output_list.sort()
print(output_list)