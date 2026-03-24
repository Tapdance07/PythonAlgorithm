# 한개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를
# 만들려고 한다. 각회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 
# 회의실을 사용할 수 있는 회의의 최대 개수

import sys

N = int(sys.stdin.readline().rstrip())
# 회의의 수
hE = list()
for _ in range(N):
    # 시작 시간과 끝나는 시간을 받는다.
    s,e = map(int,sys.stdin.readline().rstrip().split())
    # 그럼 여기서 걸리는 시간이 적은 애들이 좋은거 잖아 그래야 많이 사용할 수 있는거고
    # 그럼 걸리는 시간을 만들어야 하나 
    hE.append((e,s))
hE.sort()
last_end_time = 0
count = 0
for i in range(N):
    if hE[i][1] >= last_end_time :
        count += 1
        last_end_time = hE[i][0]
print(count)