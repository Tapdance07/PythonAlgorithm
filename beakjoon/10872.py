import sys


def Factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

N = int(sys.stdin.readline().rstrip())

print(Factorial(N))