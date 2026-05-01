import sys

def solve():
    n = int(sys.stdin.readline())
    triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    dp = triangle
    
    for i in range(1, n): # 두 번째 줄부터 시작
        for j in range(len(dp[i])):
  
            if j == 0:
                dp[i][j] += dp[i-1][0]
  
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    
    print(max(dp[n-1]))

solve()