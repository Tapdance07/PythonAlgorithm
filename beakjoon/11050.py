import sys


def Factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

N,k = map(int,sys.stdin.readline().rstrip().split())

print(Factorial(N)//Factorial(k)//Factorial(N-k))