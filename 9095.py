import sys


for T in range(int(sys.stdin.readline().rstrip())):
    n, i = int(sys.stdin.readline().rstrip()), 4
    plus = [None, 1, 2, 4]

    while i <= n:
        plus.append(plus[i - 1] + plus[i - 2] + plus[i - 3])
        i += 1

    print(plus[n])