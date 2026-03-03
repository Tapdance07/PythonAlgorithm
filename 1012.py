# from collections import deque
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)  # DFS일 경우 대비

# # 방향: 상, 하, 좌, 우
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]

# def bfs(x, y, field, visited, M, N):
#     queue = deque()
#     queue.append((x, y))
#     visited[y][x] = True

#     while queue:
#         cx, cy = queue.popleft()
#         for dir in range(4):
#             nx = cx + dx[dir]
#             ny = cy + dy[dir]
#             if 0 <= nx < M and 0 <= ny < N:
#                 if field[ny][nx] == 1 and not visited[ny][nx]:
#                     visited[ny][nx] = True
#                     queue.append((nx, ny))

# T = int(input())
# for _ in range(T):
#     M, N, K = map(int, input().split())
#     field = [[0] * M for _ in range(N)]
#     visited = [[False] * M for _ in range(N)]

#     for _ in range(K):
#         x, y = map(int, input().split())
#         field[y][x] = 1

#     count = 0
#     for y in range(N):
#         for x in range(M):
#             if field[y][x] == 1 and not visited[y][x]:
#                 bfs(x, y, field, visited, M, N)
#                 count += 1
#     print(count)

# 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 인접한 다른 배추로 이동할 수 있어,
# 그 배추들 역시 해충으로부터 보호받을 수 있다. 
# 한 배추의 상하좌우 네 방향에 다른 배추가 위한 경우에 서로 인접해 있는 것이다.
# # 배추밭은 고르지 못해서 배추가 군데 군데 심어져 있다.
# 배추들이 모여있는 곳에는 배추흰지렁이가 한마리만 있으면 된다..
# 테스트 케이스의 개수 T가 주어진다.
# 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로 길이M,N 그리고 배추가 심어져 있는 위치의 개수 K가 주어진다.
# 다음 K개의 줄에는 배추가 심어져 있는 위치의 x,y 좌표가 주어진다.
# 각 테스트 케이스에 대해 필요한 최소의 배추 흰지렁이 수를 출력한다.
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 지렁이는 위아래로 한칸씩 올라다닐수 있다


def bfs(x,y,field,visited,M,N):
    queue = deque()
    queue.append((x,y))
    visited[y][x] = True
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if filed[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((nx,ny))

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    filed = [[0]*M for _ in range(N)]
    for _ in range(K):
        x,y = map(int,input().split())
        filed[y][x] = 1
        # 배추밭을 기록하자
        visited = [[False] * M for _ in range(N)]
        # BFS나 DFS로 배추밭을 탐색하면 된다.
        
    #여기까지가 문제에서 입력 부분이고
    # 이제 BFS나 DFS로 배추밭을 탐색하자
    count = 0
    for y in range(N):
        for x in range(M):
            if filed[y][x] == 1 and not visited[y][x]:
                bfs(x,y,filed,visited,M,N)
                count += 1
    print(count)