import sys

N, M = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


INF = float('inf')
dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)]


for j in range(M):
    for d in range(3):
        dp[0][j][d] = grid[0][j]


for i in range(1, N):
    for j in range(M):
        if j > 0:
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + grid[i][j]
        

        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + grid[i][j]
        

        if j < M - 1:
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + grid[i][j]


ans = INF
for j in range(M):
    ans = min(ans, min(dp[N-1][j]))

print(ans)