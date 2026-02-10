import sys

# 입력 처리
N, M = map(int, sys.stdin.readline().rstrip().split())
Sites = {}


for _ in range(N):
    site, pwd = sys.stdin.readline().rstrip().split()
    Sites[site] = pwd

for _ in range(M):
    FSite = sys.stdin.readline().rstrip()
    print(Sites[FSite])
