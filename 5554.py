X = 0
Y = 0
A = 0
for _ in range(4):
    A += int(input())

X += A // 60
Y += A % 60
print(X)
print(Y)