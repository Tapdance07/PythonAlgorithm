import sys

N = int(sys.stdin.readline().rstrip())

dp = [False] * (max(5, N + 1))
    
dp[1] = True
dp[2] = False  
dp[3] = True
dp[4] = True
    
for i in range(5, N + 1):
        # 내가 돌을 가져간 뒤(i-1, i-3, i-4) 
        # 상대방이 지는 케이스가 하나라도 있다면 내가 이김
    if not dp[i-1] or not dp[i-3] or not dp[i-4]:
        dp[i] = True
    else:
        dp[i] = False
            
print("SK" if dp[N] else "CY")