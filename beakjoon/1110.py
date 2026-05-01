import sys

enter = int(sys.stdin.readline().rstrip())
result = enter
ans = 0
while True:
    if result//10 == 0 :
        result * 10
    A = result//10

    B = result % 10

    result = (B*10)+((A+B)%10)
    ans += 1

    if enter == result:
        break
print(ans)


