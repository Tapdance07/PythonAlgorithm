import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
jido = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dist = [[-1] * m for _ in range(n)]

queue = deque()


for i in range(n):
    for j in range(m):
        if jido[i][j] == 2:
            queue.append((i, j))
            dist[i][j] = 0  
        elif jido[i][j] == 0:
            dist[i][j] = 0  

dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

while queue:
    y, x = queue.popleft()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and dist[ny][nx] == -1:
            if jido[ny][nx] == 1:

                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny, nx))


for row in dist:
    print(*row)
