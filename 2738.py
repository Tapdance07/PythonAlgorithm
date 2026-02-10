N,M = map(int,input().split())
A = list()
B = list()
for i in range(N):
    A.append(list(map(int,input().split())))
for i in range(N):
    B.append(list(map(int,input().split())))
    for z in range(M):
        A[i][z] += B[i][z]

for i in range(N):
    for z in range(M):
        print(A[i][z],end=' ')
    print()