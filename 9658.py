import sys

N = int(sys.stdin.readline().rstrip())

dp = [False] * (max(5, N + 1))

dp[1] = False  
dp[2] = True  
dp[3] = False  
dp[4] = True  

for i in range(5, N + 1):
    
    if not dp[i-1] or not dp[i-3] or not dp[i-4]:
        dp[i] = True
    else:
        dp[i] = False

if dp[N]:
    print('SK')
else:
    print('CY')