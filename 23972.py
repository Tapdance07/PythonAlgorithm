import sys

K,N = map(int,sys.stdin.readline().rstrip().split())

if N == 1:
    print(-1)
else:
    x = (N * K) // (N - 1)
    if ((K * N) % (N - 1)):
        x += 1
    print(x)