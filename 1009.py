import sys

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10

    if a == 0:
        print(10)
    else:
        # a의 제곱 결과의 마지막 자릿수의 주기 구하기
        cycle = []
        tmp = a
        while tmp not in cycle:
            cycle.append(tmp)
            tmp = (tmp * a) % 10

        index = (b - 1) % len(cycle)
        result = cycle[index]
        if result == 0:
            print(10)
        else:
            print(result)
