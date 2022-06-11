# FizzBuzz問題
print("FizzBuzz問題")
output = ""
for i in range (1, 101):
    if i % 3 == 0:
        output = f'{output}{"Fizz"}'

    if i % 5 == 0:
        output = f'{output}{"Buzz"}'
    
    if output == "":
        output = str(i)

    print(output)
    output = ""