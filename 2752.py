import sys

N = list(map(int,sys.stdin.readline().rstrip().split()))
N.sort()
print(*N)