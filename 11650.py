N = int(input())
A = list()
for i in range(N):
    A.append(list(map(int,input().split())))

A.sort()

for i in range(len(A)):
    print(*A[i])