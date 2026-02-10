import sys
from collections import deque

N,K = map(int,sys.stdin.readline().rstrip().split())
#   N명 정수 K

YO = deque()
ans = list()
YO.extend(list(range(1,N+1)))

while True:
    if len(YO) != 0:
        for i in range(K):
            if i == K-1:
                ans.append(YO.popleft())
            else:
                YO.append(YO.popleft())
    else:
        break

print("<",end='')
print(*ans,sep=', ',end='')
print(">")