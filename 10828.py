import sys

N = int(sys.stdin.readline().rstrip())
Stack = list()
for i in range(N):
    cmd = list(sys.stdin.readline().rstrip().split())

    if cmd[0] == "push":
        Stack.append(cmd[1])

    elif cmd[0] == "pop":
        if len(Stack)>0:
            print(Stack.pop())
        else:
            print(-1)

    elif cmd[0] == "size":
        print(len(Stack))
    elif cmd[0] == "empty":
        if len(Stack)== 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "top":
        if len(Stack)>0:
            print(Stack[-1])
        else:
            print(-1)

