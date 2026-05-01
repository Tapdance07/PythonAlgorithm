import sys

def numbic(N):
    result = 0
    for i in N:
        result = result + i**2

    return result %10

T = list(map(int,sys.stdin.readline().rstrip().split()))
print(numbic(T))