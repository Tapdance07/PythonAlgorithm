import sys

N = int(sys.stdin.readline().rstrip())

Que = list()
for _ in range(N):
    cmds = list(sys.stdin.readline().rstrip().split())
    cmd = cmds[0]

    if cmd =="push":
        Que.append(cmds[1])

    elif cmd == "pop":
        if len(Que) > 0:
            print(Que[0])
            del Que[0]
        else:
            print(-1)

    elif cmd =="size":
        print(len(Que))

    elif cmd == "empty":
        if len(Que) == 0:
            print(1)
        else:
            print(0)

    elif cmd == "front":
        if len(Que) >0:
            print(Que[0])
        else:
            print(-1)

    elif cmd == "back":
        if len(Que) >0:
            print(Que[-1])
        else:
            print(-1)