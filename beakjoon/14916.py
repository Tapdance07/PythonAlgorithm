import sys

n = int(sys.stdin.readline().rstrip())

INF = float('inf')
dp = [INF] * (n+1)

dp[0] = 0

for i in range(n+1):
    
    if i>=2 and dp[i-2] != INF:
        dp[i] = dp[i-2]+1
        
    if i>=5 and dp[i-5] != INF:
        dp[i] = min(dp[i],dp[i-5]+1)
        
if dp[n] == INF:
    print(-1)
else:
    print(dp[n])