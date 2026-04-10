import sys

N = int(sys.stdin.readline().rstrip())

dp = [[0] * 3 for _ in range(N + 1)]
# 사자가 없ㄴ즌 경우, 왼쪽에만 있는 경우, 오른쪽에만 있는 경우

dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1

for i in range(2, N+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) %9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) %9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) %9901
    # 이렇게 하면 가능한 모든 상태가 기록되고
    # i번째에 있는걸 다 sum해서 보여주면 된다?
    
print(sum(dp[i]) % 9901)