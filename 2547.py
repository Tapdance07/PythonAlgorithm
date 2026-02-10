import sys


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline().rstrip())
    Candy = 0
    for _ in range(N):
        Candy += int(sys.stdin.readline().rstrip())
    if Candy%N==0:
        print("YES")
    else:
        print("NO")