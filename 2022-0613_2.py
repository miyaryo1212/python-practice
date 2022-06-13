# Pythonで模様を描く
print("Pythonで模様を描く")
N = int(input("N段のピラミッド >>> "))
for i in range(1, N + 1):
    print(f'{" "*(N-i)}{"*"*i}{"*"*(i-1)}')
