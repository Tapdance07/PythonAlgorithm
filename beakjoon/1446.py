import sys

N, D = map(int,sys.stdin.readline().rstrip().split())

                
shortcuts = []
for _ in range(N):
    start, end, dist = map(int, sys.stdin.readline().split())
    if end <= D and (end - start) > dist:
        shortcuts.append((start, end, dist))
        
dp = [i for i in range(D+1)]

for i in range(D+1):
    if i > 0:
        dp[i] = min(dp[i],dp[i-1] +1)
        
    for s,e,d in shortcuts:
        if i == s and e <= D:
            if dp[i] + d < dp[e]:
                dp[e] = dp[i] + d 
                
print(dp[D])