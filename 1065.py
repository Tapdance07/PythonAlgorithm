import sys

N = int(sys.stdin.readline())
"""N은 1000까지"""
Count = 99
if N < 100:
    print(N)
else:
    for i in range(100,N+1):
        if (i//100 - i%100//10) == (i%100//10 - i%10):
            Count += 1
        else:
            pass
    print(Count)