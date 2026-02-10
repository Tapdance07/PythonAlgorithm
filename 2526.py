import sys
N,P = map(int,sys.stdin.readline().rstrip().split())

visited = dict()  # 각 수가 처음 등장한 인덱스 저장
current = N
index = 0

while True:
    if current in visited:
        # 사이클의 시작부터 끝까지 서로 다른 수의 개수
        cycle_length = index - visited[current]
        print(cycle_length)
        break
    visited[current] = index
    current = (current * N) % P
    index += 1