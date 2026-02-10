import sys
from collections import deque

# 입력 처리
N = int(sys.stdin.readline().rstrip())
que = deque(enumerate(map(int, sys.stdin.readline().rstrip().split()), start=1))

ans = []

while que:
    idx, move = que.popleft()
    ans.append(idx)

    if que:
        if move > 0:
            que.rotate(-(move - 1))
        else:
            que.rotate(-move)


print(*ans)