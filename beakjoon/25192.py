import sys
N = int(sys.stdin.readline().rstrip())

Imoji = set()
Count = 0
for i in range(N):
    T = sys.stdin.readline().rstrip()
    if T == "ENTER":
        Count += len(Imoji)
        Imoji =set()
    else:
        if T in Imoji:
            pass
        else:
            Imoji.add(T)
Count += len(Imoji)
print(Count)