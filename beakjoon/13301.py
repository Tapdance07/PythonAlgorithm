import sys

N = int(sys.stdin.readline().rstrip())

dp = [0] * (N + 2)
dp[1] = 1
dp[2] = 1

for i in range(3, N + 2):
    dp[i] = dp[i-1] + dp[i-2]

if N == 1:
    print(4)
else:
    print((dp[N] + (dp[N] + dp[N-1])) * 2)