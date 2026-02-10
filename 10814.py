import sys

N = int(sys.stdin.readline().rstrip())
T = list()
for i in range(N):
    A,B =sys.stdin.readline().rstrip().split()
    T.append([int(A),B])
T.sort(key=lambda x:x[0])
for i in range(len(T)):
    print(*T[i])