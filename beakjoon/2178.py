# N * M 으로 표현되는 미로 풀기
# 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸
# (1,1)에서 출발하여 (N,M)으로 도착할때 지나는
# 최소한의 칸수를 구한다.

from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_y, start_x):
    queue = deque([(start_y, start_x)])
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < M:
                if miro[ny][nx] == 1:
                    miro[ny][nx] = miro[y][x] + 1
                    queue.append((ny, nx))
    
    return miro[N-1][M-1]

print(bfs(0, 0))