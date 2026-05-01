# 정사각형의 지도가 있다.
# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 연결된건 좌우 위아래로 다른집이 있는 경우를 말함
# 대각선은 미포함한다.
# 각 단지에 속하는 집의 수를 오름차순으로 정렬한다.

import sys

N = int(sys.stdin.readline().rstrip())
apt = [list(map(int, sys.stdin.readline().rstrip()))for _ in range(N)]

from collections import deque

# 일단 BFS로 먼저 풀어보자
# 값이 결국엔 전체의 리스트를 돌아봐야 하겠다.
# 일단 먼저 점을 하나씩 방문하다가 1이 아닌 곳을 방문으로 잡아야하지 않을까?
# 방문점으로 잡은 곳을 start로 잡아서 visited를 초기화하자.
visited = [[False]*N for _ in range(N)]
# 이중 리스트 구조로 만들어서 방문 테이블을 만든다.

def BFS(y, x):
    queue = deque([(y, x)])
    visited[y][x] = True
    sede = 1  # 시작점도 집이므로 1부터 시작

    while queue:
        curr_y, curr_x = queue.popleft() # 현재 위치 꺼내기

        # 상하좌우 탐색
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = curr_y + dy, curr_x + dx
            
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx] and apt[ny][nx] == 1:
                    visited[ny][nx] = True # 방문 처리
                    sede += 1              # 단지 내 세대 수 증가
                    queue.append((ny, nx)) # 다음 탐색을 위해 큐에 삽입
    return sede

result = []
for i in range(N):
    for j in range(N):
        if apt[i][j] == 1 and not visited[i][j]:
            result.append(BFS(i, j))

result.sort()
print(len(result))
for count in result:
    print(count)
        