import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
if N==0 and M == 0:
    print(0)
else:
    print(N*M-1)