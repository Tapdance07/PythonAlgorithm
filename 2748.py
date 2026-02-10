import sys

n = int(sys.stdin.readline().rstrip())

memo = {}

def fibo(n):
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibo(n-1) + fibo(n-2)
    memo[n] = result
    return result

print(fibo(n))