# うるう年の判定
input_year = int(input("うるう年を判定する (西暦) >>> "))
if input_year % 400 == 0:
    print(f'{"西暦"}{str(input_year)}{"年はうるう年です"}')
else:
    if input_year % 100 == 0:
        print(f'{"西暦"}{str(input_year)}{"年はうるう年ではありません"}')
    else:
        if input_year % 4 == 0:
                print(f'{"西暦"}{str(input_year)}{"年はうるう年です"}')
        else:
            print(f'{"西暦"}{str(input_year)}{"年はうるう年ではありません"}')
