# 폴리오미노란 크기가 1x1인 정사각형을 여러 개 이어서 붙인 도형
# 정사각형은 서로 겹치면 안된다.
# 도형은 모두 연결되어 있어야 한다.
# 정사각형의 변끼리 연결되어 있어야 한다.
# 즉 꼭짓점과 꼭짓점만 맞닿아 있으면 안된다.
# N X M 인 종이 위에 테트로미노 하나를 놓는다.
# 각 칸에는 정수가 한개 쓰여 있다.
# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 
# 최대로 하는 프로그램을 작성

import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

tetromino = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# 여기서 이제 테트로미노를 놓았을때 최대가 되는 값을 찾아야한다.
# 1 * 4 는 회전을 포함하면 2개
# 2 * 2 는 회전이 없지
# ㄴ 자는 8개의 경우의 수
# ㄹ 자는 4개의 경우의 수
# ㅗ 자는 4개의 경우의 수
# 총 19개 경우의 수가 존재하는데 이걸 DFS로 해결해본다.

# 상, 하, 좌, 우 이동을 위한 좌표
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[False] * M for _ in range(N) ]
ans = 0

def DFS(r,c,count,total):
    global ans

    # 재귀 종료 4칸 선택
    if count ==4:
        ans = max(ans,total)
        return
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<= nr <N and 0<= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            # 다음 칸으로 이동 (칸 수 +1, 합계에 현재 칸 값 추가)
            DFS(nr, nc, count + 1, total + tetromino[nr][nc])
            visited[nr][nc] = False

def check_t(r, c):
    global ans
    for i in range(4):
        # 한 방향씩 빼면서 3방향만 선택 (ㅗ, ㅜ, ㅏ, ㅓ 모양이 나옴)
        tmp = tetromino[r][c]
        is_possible = True
        for j in range(4):
            if i == j: continue # 한 방향은 제외
            nr, nc = r + dr[j], c + dc[j]
            if 0 <= nr < N and 0 <= nc < M:
                tmp += tetromino[nr][nc]
            else:
                is_possible = False
                break
        if is_possible:
            ans = max(ans, tmp)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, 1, tetromino[i][j])
        visited[i][j] = False 
        
        check_t(i, j)

print(ans)