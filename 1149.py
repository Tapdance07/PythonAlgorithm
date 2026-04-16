# RGB 거리에는 집이 N개가 있다.
# 1번 부터 N번 집이 순서대로 있다.
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야한다.
# 1번 집의 색은 2번집의 색과 같지 않아야 한다.
# N번의 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i번 집의 색은 i-1번, i+1번의 집의 색과 같지 않아야 한다.

import sys
N = int(sys.stdin.readline().rstrip())
home = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
# 0이 R, 1인 G, 2가 B다

dp = home
for i in range(1,N):
    dp[i][0] = dp[i][0] + min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = dp[i][1] + min(dp[i-1][2],dp[i-1][0])
    dp[i][2] = dp[i][2] + min(dp[i-1][0],dp[i-1][1])

print(min(dp[N-1]))