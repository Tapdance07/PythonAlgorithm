# 수빈이는 현재 점 N에 있고,
# 동생은 점 K 에 있다.
# 수빈이는 걷거나 순간이동이 가능하다.
# 수빈이의 위치가 x 일 때 걷는다면 1초 후이 x-1 또는 x+1 로 이동하게 된다
# 순간이동을 하는 경우에는 1초 후에 2*x 의 위치로 이동하게 된다
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇초 후인지 구하자

import sys
N,K = map(int, sys.stdin.readline().rstrip().split())

from collections import deque

MAX = 100001
visited = [-1] * MAX
# 이렇게 해서 이동할수 있는 걸 미리 지정해둔다.

def BFS(start):
    queue = deque([start])
    # 일단 큐에 시작지점을 넣자.

    while queue:
        curr = queue.popleft()
        if curr == K:
            return visited[curr]
        
        # 이동 가능한 세 가지 경우의 수
        for next_pos in (curr - 1, curr + 1, curr * 2):
            # 범위 내에 있고  아직 방문하지 않았다면
            if 0 <= next_pos < MAX and visited[next_pos] == -1:
                visited[next_pos] = visited[curr] + 1
                queue.append(next_pos)

print(BFS(N))