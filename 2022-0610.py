# フィボナッチ数列
print("フィボナッチ数列")
n = int(input("第何項まで (n≧2) >>> "))
a = 1
b = 1
print(a)
print(b)
n = n-2
for i in range(n):
    c = a + b
    print(c)
    b = a
    a = c