import sys

N = int(sys.stdin.readline().rstrip())
spilt_N = list(map(int,sys.stdin.readline().rstrip().split()))
if N == 1:
    print(spilt_N[0]**2)
else:
    print(max(spilt_N)*min(spilt_N))