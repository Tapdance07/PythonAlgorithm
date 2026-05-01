import sys

N = int(sys.stdin.readline().rstrip())
A = list()
for i in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))

A.sort(key=lambda x: (x[1],x[0]))

for i in range(len(A)):
    print(*A[i])