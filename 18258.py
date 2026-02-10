#큐 연산 배우기

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())


que = deque()
#큐로 사용할 리스트

for _ in range(N):
    cmd = list()
    cmds = (sys.stdin.readline().rstrip().split())
    cmd.extend(cmds)
    #명령어 저장
    if cmd[0] == 'push':
        que.append(cmd[1])

    elif cmd[0] == 'pop':
        if len(que) != 0:
            print(que.popleft())

        else:
            print(-1)

    elif cmd[0] == 'size':
        print(len(que))

    elif cmd[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front':
        if len(que) != 0:
            print(que[0])

        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(que) != 0:
            print(que[-1])

        else:
            print(-1)