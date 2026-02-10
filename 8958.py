import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    Count = 0
    Case = list(sys.stdin.readline().rstrip())
    AddCount = 1
    for i in range(len(Case)):
        if Case[i] == "O":
            if i != 0 and Case[i-1] == "O":
                AddCount += 1
            Count += AddCount
        else:
            AddCount = 1
    print(Count)