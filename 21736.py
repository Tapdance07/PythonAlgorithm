# 대학의 캠퍼스는 N * M 크기이다.
# 이동하는 방법은 벽이 아닌 상하좌우로 이동하는 것이다.
# 예를 들어 (x,y) 에 있다면 이동할 수있는 곳은 (x +1,y), (x -1,y), (x,y +1), (x,y -1) 이다.
# 캠퍼스에서 만날 수 있는 사람의 수를 출력
# DFS 와  BFS 둘다 가능하다.
# o는 빈공간, x는 벽, i는 도연이 p는 사람이다
# 아무도 못만나면 TT를 출력한다.

import sys
from collections import deque

N,M = map(int, sys.stdin.readline().rstrip().split())
visited = [[False] * M for _ in range(N)]
campus = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

start_r, start_c = -1, -1
for r in range(N):
    for c in range(M):
        if campus[r][c] == 'I':
            start_r, start_c = r, c
            break
    if start_r != -1: 
        break 


def bfs(start_r, start_c):
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    person_count = 0
    
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if campus[nr][nc] != 'X': 
                    visited[nr][nc] = True
                    if campus[nr][nc] == 'P': 
                        person_count += 1
                    queue.append((nr, nc))
    
    return person_count if person_count > 0 else "TT"

print(bfs(start_r, start_c))

