# 보관되는 토마토 중에 익고 안익은게 있다
# 토마토가 익은 곳 옆에 있는 안익은 것은 하루가 지나면 익는다 
# 토마토 위, 아래, 왼쪽, 오른쪽 , 앞 , 뒤 방향이다
# 토마토는 스스로 익지않고 대각선은 할수 없다.

import sys
from collections import deque

M,N,H = map(int,sys.stdin.readline().rstrip().split())
# M,N은 상자의 크기, H는 쌍아지는 상자의 수
# M은 가로 칸의 수, N은 세로 칸의 수
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
tomato = list()

for _ in range(H):
    layer = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    tomato.append(layer)

# 토마토 값을 받아왔다.
# 근데 여기서 토마토의 시작점을 찾아야한다.!
# 그럼 (0,0)부터 전체를 한번 보면서 해야하지 않을까? 
# 가장 고 민이 되는 지점은 2차원 리스트이니까 위 아래를 확인해야하는데
# i의 값을 H로 나눠서 사용해야하지 않을까? 몫이 결국엔 값이잖아?
# 그럼 여기서 보면 visited를 걸리는 일수로 확인을 해야해 
# 그리고 다른곳에서 그곳에 도달했을 경우에 값을 비교해서 더 적은 값으로 최신화할수 있게
# 해야해

queue = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                # 좌표를 튜플로 묶어서 삽입!
                queue.append((h, n, m))
                visited[h][n][m] == 0

def BFS():
    # 여기가 제일 중요한데 

    while queue:
        curr_z,curr_y,curr_x = queue.popleft()
        dx = [0,0,0,0,-1,1]
        dy = [0,0,-1,1,0,0]
        dz = [-1,1,0,0,0,0]

        for i in range(6):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            nz = curr_z + dz[i]
            if 0<= nx < M and 0<= ny <N and 0<= nz <H:

                if visited[nz][ny][nx] == 0 and tomato[nz][ny][nx] == 0:
                    visited[nz][ny][nx] = visited[curr_z][curr_y][curr_x] + 1
                    tomato[nz][ny][nx] = 1 # 토마토를 익은 상태로 변경
                    queue.append((nz, ny, nx))


BFS()
ans = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
        
            if tomato[h][n][m] == 0:
                print(-1)
                exit() 
            
            ans = max(ans, visited[h][n][m])

print(ans)