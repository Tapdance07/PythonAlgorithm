import sys

M = int(sys.stdin.readline().rstrip())
Set = set()

for i in range(M):
    cmds = list(sys.stdin.readline().rstrip().split())
    cmd = cmds[0]
    if cmd == "add":
        Set.add(int(cmds[1]))

    elif cmd == "remove":
        if int(cmds[1]) in Set:
            Set.remove(int(cmds[1]))
        else:
            pass

    elif cmd == "check":
        if int(cmds[1]) in Set:
            print(1)
        else:
            print(0)

    elif cmd == "toggle":
        if int(cmds[1]) in Set:
            Set.remove(int(cmds[1]))
        else:
            Set.add(int(cmds[1]))

    elif cmd == "all":
        Num = set(range(1,21))
        Set.symmetric_difference_update(Num)
        pass

    elif cmd == "empty":
        Set.clear()