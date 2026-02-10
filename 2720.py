t = int(input())
change = [25, 10, 5, 1]
result = [0] * 4

for i in range(t):
    pay = int(input())
    for j in range(len(change)):
        result[j] = pay // change[j]
        pay -= change[j] * result[j]
    print(*result)