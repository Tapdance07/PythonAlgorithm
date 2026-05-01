import sys

N = int(sys.stdin.readline().rstrip())
T = list()
for i in range(N):
    T.append(sys.stdin.readline().rstrip())

T =list(set(T))
T.sort(key=lambda x:(len(x),x))

for i in T:
    print(i)