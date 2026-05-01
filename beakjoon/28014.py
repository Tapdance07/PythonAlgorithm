import sys
Input  = sys.stdin.readline
N = int(Input().rstrip())
Top = list(map(int,Input().rstrip().split()))
result = 1
i = 0
while i < N-1:
    if Top[i] <= Top[i+1]:
        result += 1
    i += 1
print(result)