import sys

N, M = map(int, sys.stdin.readline().split())
col_has_guard = [False] * M  # 각 열에 X가 있는지 여부 저장
row_guard = 0

for _ in range(N):
    line = sys.stdin.readline().strip()
    if 'X' not in line:
        row_guard += 1  # 이 행에는 경비원이 필요함
    for j in range(M):
        if line[j] == 'X':
            col_has_guard[j] = True  # 해당 열은 경비원이 있음

# 열 중 경비원이 하나도 없는 열 세기
col_guard = col_has_guard.count(False)

print(max(row_guard, col_guard))