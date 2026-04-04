# 토마토 상자 문제

import sys
from collections import deque

M,N = map(int,sys.stdin.readline().rstrip().split())
tomato = list()

for _ in range(N):
    tomato.append(list(map(int,sys.stdin.readline().rstrip().split())))

visited = [[0] * M for _ in range(N) ]
# 여기까지가 기본 세팅

# 토마토 위치 찾기 

queue = deque()
# 큐 만들고
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i,j))

def BFS():
    
    while queue:
        curr_y, curr_x = queue.popleft()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4):
            nx,ny = curr_x + dx[i], curr_y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if visited[ny][nx] == 0 and tomato[ny][nx] == 0:
                    visited[ny][nx] = visited[curr_y][curr_x] + 1
                    tomato[ny][nx] = 1
                    queue.append((ny,nx))

BFS()

ans = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit()
        else:
            ans = max(ans,visited[i][j])
if ans == 0:
    print(0)
else:
    print(ans)