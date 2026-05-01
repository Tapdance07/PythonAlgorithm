import sys
from collections import deque


N = int(sys.stdin.readline().rstrip())
Deque = deque()

Deque.extend(list(range(1, N + 1)))

while True:
    if len(Deque) != 1:
        Deque.popleft()
        Deque.append(Deque.popleft())
    else:
        break
print(Deque[0])