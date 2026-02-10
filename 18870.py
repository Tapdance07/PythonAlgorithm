import sys

N = int(sys.stdin.readline().rstrip())

T = list(map(int,sys.stdin.readline().rstrip().split()))
T_idx = list()
for i in range(N):
    T_idx.append([i, T[i]])
    
T_idx.sort(key=lambda x : x[1])

cnt = -1
tmp = float("INF")
for i in range(N):
    if tmp != T_idx[i][1]:
        cnt += 1
        tmp = T_idx[i][1]

    T_idx[i][1] = cnt

T_idx.sort()
for _, a in T_idx:
    print(a, end=' ')
print()