import sys

T = int(sys.stdin.readline().rstrip())

def Factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

for i in range(T):
    N,M = map(int,sys.stdin.readline().rstrip().split())
    print(Factorial(M) // Factorial(N) // Factorial(M - N))