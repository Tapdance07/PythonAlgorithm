N = int(input())
S = list(map(int,input().split()))
print(len(S) - len(set(S)))