# 최대 힙
# 배열에 자연수 x를 넣는다
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 연산의 개수 N이 주어진다
# 다음 N개의 줄에는 연산에 대한 정보를 나타내느 ㅈ어수 x가 주어진다.
# x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거한다.

import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)