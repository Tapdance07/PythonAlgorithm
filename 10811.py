N,M = map(int,input().split())
B = []

for z in range(N):
    B.append(z+1)

for _ in range(M):
    i,j = map(int, input().split())
    B[i-1:j] = reversed(B[i-1:j])
print(*B)
