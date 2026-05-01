# 경로찾기
# 갖우치 없는 방향 그래프 G가 주어졌을 때 모든 정점 (I,j)에 대해서 
# I에서 J로 가는 길이가 양수인 경로가 있는지 없는 구하는 프로그램

import sys
N = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

# k = 거쳐가는 노드
# i = 출발 노드
# j = 도착 노드
for k in range(N):
    for i in range(N):
        for j in range(N):
            # i에서 k로 갈 수 있고, k에서 j로 갈 수 있다면
            # i에서 j로 가는 경로가 존재한다고 판단!
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for row in graph:
    print(*row)