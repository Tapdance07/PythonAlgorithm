# 적록 색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다.
# 크기가 N*N 인 그리드의 각 칸에 R,G,B 주 ㅇ하나를 색칠한 그림이 있다.
# 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다.
# 또 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다.
# 적록색약인 사람과 아닌 사람의 보는 구역의 갯수의 차이

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
color = list()

for _ in range(N):
    color.append(list(sys.stdin.readline().rstrip()))

visited = [[0]*N for _ in range(N)]
# 데이터 받기 완료
# BFS를 먼저 해볼까


def BFS(y,x,site_color):
    queue = deque([(y,x)])
    
    visited[y][x] = 1
    
    while queue:
        curr_y, curr_x = queue.popleft()
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            ny,nx = curr_y + dy[i], curr_x + dx[i]
            # 상하좌우의 좌표 갱신
            if 0<= nx < N and 0<= ny < N:
                if color[ny][nx] == site_color:
                    if visited[ny][nx] == 0:
                        
                        visited[ny][nx] = 1
                        queue.append((ny,nx))


nomal = 0
notnomal = 0
# 그럼 먼저 각 색의 시작지점을 다 맞춰서 해야겠지
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i,j,color[i][j])
            nomal += 1

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if color[i][j] == 'G':
            color[i][j] = 'R'
            
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i,j,color[i][j])
            notnomal += 1
print(nomal,notnomal)