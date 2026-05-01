import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    Que = deque((value, idx) for idx, value in enumerate(A))

    Count = 0

    while True:

        if Que[0][0] == max(Que, key=lambda x: x[0])[0]:
            Count += 1  # 문서를 처리함
            value, idx = Que.popleft()
            if idx == M:
                print(Count)
                break
        else:
            Que.rotate(-1)
