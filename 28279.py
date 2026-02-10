import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
Que = deque()
for _ in range(N):
    cmd = list(map(int,sys.stdin.readline().rstrip().split()))
    if cmd[0] == 1:
        Que.appendleft(cmd[1])
    elif cmd[0] == 2:
        Que.append(cmd[1])
    elif cmd[0] == 3:
        print(Que.popleft() if len(Que)>0 else -1)
    elif cmd[0] == 4:
        print(Que.pop() if len(Que) > 0 else -1)
    elif cmd[0] == 5:
        print(len(Que))
    elif cmd[0] == 6:
        print(print(1) if len(Que)==0 else 0)
    elif cmd[0] == 7:
        print(Que[0] if len(Que) > 0 else -1)
    elif cmd[0] == 8:
        print(Que[-1] if len(Que) > 0 else -1)