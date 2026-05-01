import sys

N = int(sys.stdin.readline().rstrip())

miro = list(map(int,sys.stdin.readline().rstrip().split()))
INF = float('inf')
dp = [INF] * N
dp[0] = 0

for i in range(N):
    if dp[i] == INF: continue
    for j in range (1,miro[i]+1):
        if i + j < N:
            dp[i + j] = min(dp[i + j], dp[i] + 1)
            
if dp[N-1] == INF:
    print(-1)
else:
    print(dp[N-1])