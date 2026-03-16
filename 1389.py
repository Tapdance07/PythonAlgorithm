# 지구에 있는 모든 사람들은 최대 6단계 이내에서 서로 아는 사람으로 연결될 수 있다.
# 케빈 베이컨 게임은 임의의 두 사람이 최소 몇 단계 만에 이어질수 있는지 계산
# 케빈 베이컨은 미국 헐리우드 영화배우들 끼리 케빈 베이컨 게임을 했을때 나오는 단계의 총합이 가장 적은 사람
#  케빈 베이컨의 수 가 가장 작은 사람을 구하는 프로그램
# 첫번째 줄에 유저의 수 N 과 친구 관계의 수 M이 주어진다.
# 둘째 줄부터 M개의 줄에는 친구 관계가 주어진다.
# 친구관계는 중복되어 들어올 수도 있다.
# 모든 사람은 친구관계로 연결되어져 있다.
# 즉 모든 사람과 거치는 관게가 제일 적은 사람
import sys
from collections import deque

N, M = map(int,sys.stdin.readline().rstrip().split())
node = [[] for _ in range(N + 1)]
# 빈공간 만들기
# 어떤 사람이 어디에 연결되어있는지를 확인


for _ in range(M):
    user, freind = map(int,sys.stdin.readline().rstrip().split())
    node[user].append(freind)
    node[freind].append(user)
# 여기까지가 일단적인 로직이다.


def bfs(start):
    # 각 유저까지의 단계를 기록 (미방문은 -1)
    distances = [-1] * (N + 1)
    # 한명에 대한 것
    queue = deque([start])

    distances[start] = 0  # 자기 자신까지의 거리는 0
    
    while queue:
        curr = queue.popleft()
        
        for neighbor in node[curr]:
            if distances[neighbor] == -1:  # 아직 방문하지 않은 친구라면
                distances[neighbor] = distances[curr] + 1
                queue.append(neighbor)
                
    return sum(distances[1:])

results = []
for i in range(1, N + 1):
    results.append(bfs(i))

print(results.index(min(results)) + 1)
